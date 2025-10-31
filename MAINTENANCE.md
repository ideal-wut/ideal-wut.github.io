# IDEAL智能大数据管理与分析实验室网站维护文档

## 目录
1. [项目概述](#项目概述)
2. [项目结构](#项目结构)
3. [开发环境设置](#开发环境设置)
4. [内容管理](#内容管理)
5. [部署流程](#部署流程)
6. [常见维护任务](#常见维护任务)
7. [故障排除](#故障排除)
8. [文件组织和命名规范](#文件组织和命名规范)

## 项目概述

这是一个基于Jekyll的学术实验室网站，用于展示IDEAL智能大数据管理与分析实验室的研究成果、团队成员、新闻动态等信息。


### 主要功能
- 首页展示和实验室简介
- 团队成员管理
- 研究方向展示
- 学术成果发布
- 新闻动态更新
- 招聘信息发布

## 项目结构

```
ideal-wut.github.io/
├── _config.yml              # Jekyll配置文件
├── _data/                   # 数据文件目录
│   ├── advisor.yml          # 导师信息
│   ├── alumni.yml           # 校友信息
│   ├── papers.yml           # 学术论文数据
│   ├── students.yml         # 学生信息
│   └── teachers.yml         # 教师信息
├── _includes/               # 页面组件
│   ├── footer.html          # 页脚组件
│   └── header.html          # 页头组件
├── _layouts/                # 页面布局模板
│   ├── default.html         # 默认布局
│   ├── home.html            # 首页布局
│   ├── page.html            # 普通页面布局
│   ├── post.html            # 博客文章布局
│   └── research_article.html # 研究文章布局
├── _posts/                  # 博客文章
├── _research_articles/      # 研究方向文章
│   ├── graph-database.md
│   ├── new-database-technologies.md
│   ├── spatio-temporal-database.md
│   └── vector-database.md
├── assets/                  # 静态资源
│   ├── css/style.css        # 自定义样式
│   ├── images/              # 图片资源
│   └── js/main.js           # JavaScript文件
├── achievements/            # 学术成果页面
├── blog/                    # 博客页面
├── research/                # 研究方向页面
├── team/                    # 团队页面
├── joinus.html              # 招聘页面
└── index.markdown           # 首页
```

## 开发环境设置

### 前置要求
- Ruby (推荐版本 2.7+)
- Bundler
- Git

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/ideal-wut/ideal-wut.github.io.git
   cd ideal-wut.github.io
   ```

2. **安装依赖**
   ```bash
   bundle install
   ```

3. **启动开发服务器**
   ```bash
   bundle exec jekyll serve
   ```
   或者指定主机和端口：
   ```bash
   bundle exec jekyll serve --host 0.0.0.0 --port 4000
   ```

4. **访问网站**
   打开浏览器访问 `http://localhost:4000`

### 开发工具推荐
- **代码编辑器**: VS Code, Sublime Text, Atom
- **Markdown编辑器**: Typora, Mark Text
- **图片编辑**: GIMP, Photoshop
- **版本控制**: Git

## 内容管理

### 1. 团队成员管理

#### 添加新成员
编辑对应的YAML文件：
- `_data/advisor.yml` - 导师信息
- `_data/teachers.yml` - 教师信息  
- `_data/students.yml` - 学生信息
- `_data/alumni.yml` - 校友信息

**格式示例**:
```yaml
- name: "张三"
  title: "博士研究生"
  research: "图数据库, 时空数据挖掘"
  email: "zhangsan@whut.edu.cn"
  image: "/assets/images/team/zhangsan.jpg"
  homepage: "https://example.com"
```

#### 添加成员照片
1. 将照片放入 `assets/images/team/` 目录
3. 格式: JPG或PNG
4. 文件名: 使用英文名或拼音，如 `zhangsan.jpg`

### 2. 学术成果管理

#### 添加新论文
编辑 `_data/papers.yml` 文件，在文件开头添加新论文：

```yaml
- title: "论文标题"
  authors: "作者1, 作者2, 作者3"
  venue: "会议或期刊名称"
  year: 2025
  pages: "1-10"
  doi: "10.1000/example"
  url: "https://doi.org/10.1000/example"
```

#### 使用BibTeX转换工具
项目提供了BibTeX到YAML的转换脚本：
```bash
python scripts/bibtex_to_papers_yml.py input.bib
```

### 3. 研究方向管理

#### 添加新研究方向
1. 在 `_research_articles/` 目录创建新的Markdown文件
2. 文件名格式: `research-topic-name.md`
3. 文件内容格式:

```markdown
---
title: "研究方向标题"
permalink: /research/articles/research-topic-name/
---

# 研究方向标题

研究方向的详细描述...

## 主要研究内容
- 内容1
- 内容2

## 相关论文
- 论文1
- 论文2
```

#### 修改现有研究方向
直接编辑 `_research_articles/` 目录下的对应文件。

### 4. 新闻动态管理

#### 发布新闻
1. 在 `_posts/` 目录创建新文件
2. 文件名格式: `YYYY-MM-DD-title.md`
3. 文件内容格式:

```markdown
---
layout: post
title: "新闻标题"
date: 2025-01-15 10:00:00 +0800
categories: news
---

新闻内容...
```

### 5. 图片资源管理

#### 图片存储位置
- 团队照片: `assets/images/team/`
- 轮播图片: `assets/images/carousel/`
- 研究相关: `assets/images/research/`
- 其他图片: `assets/images/`




