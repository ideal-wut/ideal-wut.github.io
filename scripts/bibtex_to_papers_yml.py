#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parse a BibTeX file (e.g., 4895.bib) and convert to _data/papers.yml
- No external APIs are used
- Minimal dependencies (pure Python)
- Supports common fields: title, author, journal/booktitle, year, volume, number/issue, pages, doi, url
- Deduplicates by DOI (or title+year when DOI missing)
- Formats authors as "Given Family" and joins with comma
"""
import re
import os
from typing import List, Dict, Optional

BIB_FILE = "4895.bib"
OUTPUT_YAML = "_data/papers.yml"

ENTRY_START_RE = re.compile(r"^\s*@\w+\s*\{\s*[^,]+,\s*$")
FIELD_RE = re.compile(r"(\w+)\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|\"(?:[^\"]|\\\")*\")\s*,?\s*$", re.DOTALL)


def read_entries(text: str) -> List[str]:
    entries = []
    buf = []
    brace_level = 0
    for line in text.splitlines():
        if ENTRY_START_RE.match(line):
            # flush previous
            if buf:
                entries.append("\n".join(buf))
                buf = []
                brace_level = 0
        buf.append(line)
        brace_level += line.count("{") - line.count("}")
        if brace_level <= 0 and buf:
            entries.append("\n".join(buf))
            buf = []
            brace_level = 0
    if buf:
        entries.append("\n".join(buf))
    return entries


def parse_fields(entry_text: str) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    # Skip the first line with @type{key,
    lines = entry_text.splitlines()[1:]
    current = ""
    for line in lines:
        if not line.strip():
            continue
        current += (line + "\n")
        # Try to match a field when line ends with ',' or '}'
        m = FIELD_RE.search(current)
        if m:
            key, raw_val = m.group(1).lower(), m.group(2)
            val = raw_val.strip()
            if val.startswith("{") and val.endswith("}"):
                val = val[1:-1]
            elif val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            # Normalize spaces
            val = re.sub(r"\s+", " ", val).strip()
            fields[key] = val
            current = ""
    return fields


def format_authors(authors_field: str) -> str:
    if not authors_field:
        return ""
    parts = [p.strip() for p in authors_field.split(" and ")]
    names = []
    for p in parts:
        if not p:
            continue
        # Handle "Last, First" or "First Last"
        if "," in p:
            last, first = [s.strip() for s in p.split(",", 1)]
            name = f"{first} {last}".strip()
        else:
            name = p.strip()
        names.append(name)
    return ", ".join(names)


def shorten_booktitle(bt: str) -> str:
    bt_clean = re.sub(r"[{}]", "", bt or "").strip()
    bt_upper = bt_clean.upper()
    # Direct abbreviation keyword scan
    abbrs = [
        "ICDE", "SIGMOD", "VLDB", "PVLDB", "CIKM", "SIGIR", "ICDM",
        "KDD", "WWW", "WSDM", "AAAI", "IJCAI", "EDBT", "DASFAA",
        "SSDBM", "SOCC", "SIGSPATIAL", "MDM"
    ]
    for ab in abbrs:
        if ab in bt_upper:
            return ab
    # Phrase mapping (case-insensitive)
    phrases = [
        (r"international conference on data engineering", "ICDE"),
        (r"information and knowledge management", "CIKM"),
        (r"knowledge discovery and data mining", "KDD"),
        (r"research and development in information retrieval", "SIGIR"),
        (r"international conference on data mining", "ICDM"),
        (r"advances in geographic information systems", "SIGSPATIAL"),
        (r"mobile data management", "MDM"),
        (r"world wide web", "WWW"),
        (r"web conference", "WWW"),
        (r"database systems", "SIGMOD"),
        (r"very large data bases", "VLDB"),
    ]
    bt_lower = bt_clean.lower()
    for pat, ab in phrases:
        if re.search(pat, bt_lower):
            return ab
    # Fallback: strip trailing location/date segments after a year like ', 2022, ...'
    # Keep text up to the first year occurrence if present
    m = re.search(r"(.*?)(19\\d{2}|20\\d{2})", bt_clean)
    if m:
        prefix = m.group(1).strip()
        # Try to extract abbr from prefix again
        prefix_upper = prefix.upper()
        for ab in abbrs:
            if ab in prefix_upper:
                return ab
        bt_clean = prefix
    # Otherwise return a compacted version (collapse spaces/commas)
    return re.sub(r"\\s*,\\s*", ", ", bt_clean)


def build_venue(fields: Dict[str, str]) -> str:
    journal = fields.get("journal")
    if journal:
        return journal.strip()
    booktitle = fields.get("booktitle")
    if booktitle:
        return shorten_booktitle(booktitle)
    publisher = fields.get("publisher") or ""
    return publisher.strip()


def build_volume_issue_pages(fields: Dict[str, str]) -> Optional[str]:
    volume = (fields.get("volume") or "").strip()
    number = (fields.get("number") or fields.get("issue") or "").strip()
    pages = (fields.get("pages") or "").strip()
    vip = None
    if volume and number and pages:
        vip = f"{volume}({number}): {pages}"
    elif volume and pages:
        vip = f"{volume}: {pages}"
    elif pages:
        vip = pages
    return vip or None


def record_from_fields(fields: Dict[str, str]) -> Dict[str, str]:
    title = (fields.get("title") or "").strip()
    authors = format_authors(fields.get("author") or "")
    venue = build_venue(fields)
    year = fields.get("year")
    try:
        year_int = int(re.findall(r"\d{4}", year or "")[0]) if year else None
    except Exception:
        year_int = None
    vip = build_volume_issue_pages(fields)
    doi = fields.get("doi")
    url = fields.get("url")

    rec: Dict[str, str] = {
        "title": title,
        "authors": authors,
        "venue": venue,
    }
    if vip:
        rec["volume_issue_pages"] = vip
    if year_int:
        rec["year"] = year_int
    if doi:
        rec["doi"] = f"https://doi.org/{doi.strip()}"
    elif url:
        rec["url"] = url.strip()
    return rec


def parse_bibtex(text: str) -> List[Dict[str, str]]:
    entries_text = read_entries(text)
    records: List[Dict[str, str]] = []
    seen = set()
    for et in entries_text:
        fields = parse_fields(et)
        rec = record_from_fields(fields)
        if not rec.get("title"):
            continue
        key = (fields.get("doi") or "") or (rec.get("title", "") + "|" + str(rec.get("year", "")))
        if key in seen:
            continue
        seen.add(key)
        records.append(rec)
    # Sort by year desc then title
    records.sort(key=lambda r: (r.get("year", 0), r.get("title", "")), reverse=True)
    return records


def dump_yaml(records: List[Dict[str, str]]) -> str:
    lines: List[str] = []
    for r in records:
        lines.append("- title: " + repr(r.get("title", "")))
        lines.append("  authors: " + repr(r.get("authors", "")))
        lines.append("  venue: " + repr(r.get("venue", "")))
        if "volume_issue_pages" in r:
            lines.append("  volume_issue_pages: " + repr(r.get("volume_issue_pages", "")))
        if "year" in r and r.get("year"):
            lines.append(f"  year: {r['year']}")
        if "doi" in r:
            lines.append("  doi: " + repr(r.get("doi", "")))
        if "url" in r:
            lines.append("  url: " + repr(r.get("url", "")))
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main():
    if not os.path.exists(BIB_FILE):
        raise SystemExit(f"BibTeX file not found: {BIB_FILE}")
    with open(BIB_FILE, "r", encoding="utf-8") as f:
        text = f.read()
    records = parse_bibtex(text)
    yaml_text = dump_yaml(records)
    with open(OUTPUT_YAML, "w", encoding="utf-8") as f:
        f.write(yaml_text)
    print(f"Wrote {len(records)} records to {OUTPUT_YAML}")

if __name__ == "__main__":
    main()