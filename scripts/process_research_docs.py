#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from docx import Document
import re

def docx_to_markdown(docx_path, image_prefix=""):
    """
    将Word文档转换为Markdown格式，为图片添加占位符
    """
    try:
        doc = Document(docx_path)
        markdown_content = []
        image_counter = 1
        
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if not text:
                continue
                
            # 检查段落样式
            style_name = paragraph.style.name if paragraph.style else ""
            
            # 处理标题
            if "Heading 1" in style_name or "标题 1" in style_name or text.endswith("：") or text.endswith(":"):
                if len(text) < 50:  # 短文本可能是标题
                    markdown_content.append(f"## {text.rstrip('：:')}")
                    markdown_content.append("")
                    continue
            elif "Heading 2" in style_name or "标题 2" in style_name:
                markdown_content.append(f"### {text}")
                markdown_content.append("")
                continue
            elif "Heading 3" in style_name or "标题 3" in style_name:
                markdown_content.append(f"#### {text}")
                markdown_content.append("")
                continue
            
            # 检查是否是列表项
            if re.match(r'^[\d\w\u4e00-\u9fff]+[\.、\)]\s*', text):
                markdown_content.append(f"- {text}")
            elif text.startswith("•") or text.startswith("-") or text.startswith("*"):
                markdown_content.append(f"- {text.lstrip('•-* ')}")
            else:
                # 普通段落
                markdown_content.append(text)
            
            # 在某些段落后添加图片占位符
            if image_prefix and (
                "方法" in text or "算法" in text or "技术" in text or 
                "系统" in text or "框架" in text or "模型" in text or
                len(text) > 100  # 长段落后可能需要图片说明
            ):
                if image_counter <= 11:  # 根据实际图片数量调整
                    img_name = f"{image_prefix}{image_counter}"
                    # 检查图片文件扩展名
                    img_path = f"/Users/jiaxu/Documents/GitHub/ideal-wut.github.io/研究方向文档/WPS图片批量处理/{img_name}"
                    if os.path.exists(f"{img_path}.png"):
                        ext = "png"
                    elif os.path.exists(f"{img_path}.jpg"):
                        ext = "jpg"
                    elif os.path.exists(f"{img_path}.jpeg"):
                        ext = "jpeg"
                    else:
                        ext = "png"  # 默认
                    
                    markdown_content.append("")
                    markdown_content.append(f"![{image_prefix}相关技术图{image_counter}](../assets/images/research/{img_name}.{ext})")
                    image_counter += 1
            
            markdown_content.append("")
        
        return "\n".join(markdown_content)
        
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return None

def update_research_file(md_path, new_content):
    """
    更新研究方向Markdown文件，保留front matter
    """
    # 读取现有文件的front matter
    front_matter = ""
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---'):
            end_index = content.find('---', 3)
            if end_index != -1:
                front_matter = content[:end_index + 3]
    
    # 写入新内容
    full_content = front_matter + "\n\n" + new_content
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Updated {md_path}")

def main():
    # Word文档目录
    docs_dir = "/Users/jiaxu/data/website/WUT/研究方向文档"
    
    # 研究方向文件目录
    articles_dir = "/Users/jiaxu/Documents/GitHub/ideal-wut.github.io/_research_articles"
    
    # 处理向量数据库
    docx_path = os.path.join(docs_dir, "向量数据库方向.docx")
    if os.path.exists(docx_path):
        print("Processing 向量数据库方向.docx...")
        content = docx_to_markdown(docx_path, "向量数据库")
        if content:
            md_path = os.path.join(articles_dir, "vector-search.md")
            update_research_file(md_path, content)
    
    # 处理图计算/图数据库
    docx_path = os.path.join(docs_dir, "图计算方向.docx")
    if os.path.exists(docx_path):
        print("Processing 图计算方向.docx...")
        content = docx_to_markdown(docx_path, "图计算")
        if content:
            md_path = os.path.join(articles_dir, "graph-database.md")
            update_research_file(md_path, content)
    
    # 处理时空数据库
    docx_path = os.path.join(docs_dir, "时空数据库.docx")
    if os.path.exists(docx_path):
        print("Processing 时空数据库.docx...")
        content = docx_to_markdown(docx_path, "时空数据库")
        if content:
            md_path = os.path.join(articles_dir, "spatio-temporal.md")
            update_research_file(md_path, content)
    
    # 处理数据库新技术（合并多个文档）
    new_tech_docs = [
        ("时序方向.docx", "时序"),
        ("AI4DB方向.docx", "AI4DB"),
        ("AI4DB-Text2SQL.docx", "AI4DB-Text2SQL"),
        ("存储器方向.docx", "存储器方向")
    ]
    
    combined_content = []
    for docx_file, image_prefix in new_tech_docs:
        docx_path = os.path.join(docs_dir, docx_file)
        if os.path.exists(docx_path):
            print(f"Processing {docx_file}...")
            content = docx_to_markdown(docx_path, image_prefix)
            if content:
                # 添加子标题
                section_title = docx_file.replace('.docx', '').replace('方向', '')
                combined_content.append(f"## {section_title}")
                combined_content.append("")
                combined_content.append(content)
                combined_content.append("")
    
    if combined_content:
        md_path = os.path.join(articles_dir, "time-series.md")
        final_content = "\n".join(combined_content)
        update_research_file(md_path, final_content)

if __name__ == "__main__":
    main()