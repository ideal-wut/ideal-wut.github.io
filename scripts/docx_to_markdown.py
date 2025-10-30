#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from docx import Document
import re

def docx_to_markdown(docx_path):
    """
    将Word文档转换为Markdown格式
    """
    try:
        doc = Document(docx_path)
        markdown_content = []
        
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if not text:
                continue
                
            # 检查段落样式
            style_name = paragraph.style.name if paragraph.style else ""
            
            # 处理标题
            if "Heading 1" in style_name or "标题 1" in style_name:
                markdown_content.append(f"# {text}")
            elif "Heading 2" in style_name or "标题 2" in style_name:
                markdown_content.append(f"## {text}")
            elif "Heading 3" in style_name or "标题 3" in style_name:
                markdown_content.append(f"### {text}")
            elif "Heading 4" in style_name or "标题 4" in style_name:
                markdown_content.append(f"#### {text}")
            else:
                # 普通段落
                # 检查是否是列表项（以数字、字母或符号开头）
                if re.match(r'^[\d\w\u4e00-\u9fff]+[\.、\)]\s*', text):
                    markdown_content.append(f"- {text}")
                elif text.startswith("•") or text.startswith("-") or text.startswith("*"):
                    markdown_content.append(f"- {text.lstrip('•-* ')}")
                else:
                    markdown_content.append(text)
            
            markdown_content.append("")  # 添加空行
        
        return "\n".join(markdown_content)
        
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return None

def main():
    # Word文档目录
    docs_dir = "/Users/jiaxu/data/website/WUT/研究方向文档"
    
    # 文档映射关系
    doc_mapping = {
        "向量数据库方向.docx": "vector-search.md",
        "图计算方向.docx": "graph-database.md", 
        "时空数据库.docx": "spatio-temporal.md",
        "时序方向.docx": "time-series.md",
        "AI4DB方向.docx": "time-series.md",  # AI4DB合并到数据库新技术
        "AI4DB-Text2SQL.docx": "time-series.md",  # Text2SQL合并到数据库新技术
        "存储器方向.docx": "time-series.md"  # 存储器方向合并到数据库新技术
    }
    
    results = {}
    
    for docx_file, md_file in doc_mapping.items():
        docx_path = os.path.join(docs_dir, docx_file)
        if os.path.exists(docx_path):
            print(f"Processing {docx_file}...")
            content = docx_to_markdown(docx_path)
            if content:
                if md_file not in results:
                    results[md_file] = []
                results[md_file].append({
                    'source': docx_file,
                    'content': content
                })
            else:
                print(f"Failed to process {docx_file}")
        else:
            print(f"File not found: {docx_path}")
    
    # 输出结果
    for md_file, contents in results.items():
        print(f"\n=== {md_file} ===")
        for item in contents:
            print(f"\n--- From {item['source']} ---")
            print(item['content'][:500] + "..." if len(item['content']) > 500 else item['content'])

if __name__ == "__main__":
    main()