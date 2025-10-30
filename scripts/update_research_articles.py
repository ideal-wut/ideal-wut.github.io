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
                markdown_content.append(f"## {text}")
            elif "Heading 2" in style_name or "标题 2" in style_name:
                markdown_content.append(f"### {text}")
            elif "Heading 3" in style_name or "标题 3" in style_name:
                markdown_content.append(f"#### {text}")
            elif "Heading 4" in style_name or "标题 4" in style_name:
                markdown_content.append(f"##### {text}")
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

def read_existing_front_matter(md_path):
    """
    读取现有Markdown文件的front matter
    """
    if not os.path.exists(md_path):
        return ""
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取front matter
    if content.startswith('---'):
        end_index = content.find('---', 3)
        if end_index != -1:
            return content[:end_index + 3]
    
    return ""

def update_markdown_file(md_path, new_content, front_matter):
    """
    更新Markdown文件
    """
    full_content = front_matter + "\n\n" + new_content
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Updated {md_path}")

def main():
    # Word文档目录
    docs_dir = "/Users/jiaxu/data/website/WUT/研究方向文档"
    
    # 研究方向文件目录
    articles_dir = "/Users/jiaxu/Documents/GitHub/ideal-wut.github.io/_research_articles"
    
    # 文档映射关系
    doc_mapping = {
        "向量数据库方向.docx": "vector-search.md",
        "图计算方向.docx": "graph-database.md", 
        "时空数据库.docx": "spatio-temporal.md",
    }
    
    # 数据库新技术相关文档（合并处理）
    new_tech_docs = [
        "时序方向.docx",
        "AI4DB方向.docx", 
        "AI4DB-Text2SQL.docx",
        "存储器方向.docx"
    ]
    
    # 处理单独映射的文档
    for docx_file, md_file in doc_mapping.items():
        docx_path = os.path.join(docs_dir, docx_file)
        md_path = os.path.join(articles_dir, md_file)
        
        if os.path.exists(docx_path):
            print(f"Processing {docx_file} -> {md_file}")
            
            # 读取Word文档内容
            content = docx_to_markdown(docx_path)
            if content:
                # 读取现有front matter
                front_matter = read_existing_front_matter(md_path)
                
                # 更新文件
                update_markdown_file(md_path, content, front_matter)
            else:
                print(f"Failed to process {docx_file}")
        else:
            print(f"File not found: {docx_path}")
    
    # 处理数据库新技术相关文档（合并）
    combined_content = []
    for docx_file in new_tech_docs:
        docx_path = os.path.join(docs_dir, docx_file)
        if os.path.exists(docx_path):
            print(f"Processing {docx_file} for time-series.md")
            content = docx_to_markdown(docx_path)
            if content:
                combined_content.append(f"## {docx_file.replace('.docx', '')}")
                combined_content.append("")
                combined_content.append(content)
                combined_content.append("")
    
    if combined_content:
        md_path = os.path.join(articles_dir, "time-series.md")
        front_matter = read_existing_front_matter(md_path)
        final_content = "\n".join(combined_content)
        update_markdown_file(md_path, final_content, front_matter)

if __name__ == "__main__":
    main()