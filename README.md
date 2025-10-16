# 实验室网站

基于 Jekyll 构建的实验室网站，包含动态发布、研究方向展示、团队成员介绍和研究成果展示等功能。

## 目录结构

```
.
├── _config.yml              # Jekyll 配置文件
├── _layouts/                # 页面布局模板
│   ├── default.html         # 默认布局
│   ├── home.html           # 首页布局
│   ├── page.html           # 普通页面布局
│   ├── post.html           # 博客文章布局
│   └── research_article.html # 研究方向文章布局
├── _includes/              # 可重用的页面组件
│   ├── header.html         # 网站头部
│   └── footer.html         # 网站底部
├── _posts/                 # 博客文章
│   └── 2025-01-15-welcome.md
├── _research_articles/     # 研究方向文章
│   ├── time-series.md
│   ├── spatio-temporal.md
│   └── vector-search.md
├── _data/                  # 数据文件
│   ├── advisor.yml         # 导师信息
│   ├── students.yml        # 在读学生信息
│   ├── alumni.yml          # 已毕业学生信息
│   └── papers.yml          # 论文列表
├── assets/                 # 静态资源
│   ├── css/
│   │   └── style.css       # 样式文件
│   ├── js/
│   │   └── main.js         # JavaScript 文件
│   └── images/             # 图片文件
│       ├── carousel/       # 轮播图
│       └── team/           # 团队成员照片
├── blog/                   # 动态列表页
├── research/               # 研究方向总览页
├── team/                   # 团队页面
│   ├── index.html          # 指导教师
│   ├── students.html       # 在读学生
│   └── alumni.html         # 已毕业学生
├── achievements/           # 研究成果页
├── joinus.md              # 加入我们页
└── index.markdown         # 首页

## URL 结构

- 首页: `/`
- 动态列表: `/blog/`
- 动态详情: `/blog/:title/`
- 研究方向总览: `/research/`
- 研究方向文章: `/research/articles/:name/`
- 指导教师: `/team/`
- 在读学生: `/team/students/`
- 已毕业学生: `/team/alumni/`
- 研究成果: `/achievements/`
- 加入我们: `/joinus/`


## 使用方法

### 1. 安装依赖

```bash
bundle install
```

### 2. 本地运行

```bash
bundle exec jekyll serve
```

访问 `http://localhost:4000` 查看网站。

### 3. 添加内容

#### 添加博客文章
在 `_posts/` 目录下创建文件，命名格式：`YYYY-MM-DD-title.md`

```markdown
---
layout: post
title: "文章标题"
date: 2025-01-15
author: 作者名
---

文章内容...
```

#### 添加研究方向文章
在 `_research_articles/` 目录下创建 Markdown 文件

```markdown
---
layout: research_article
title: 研究方向标题
description: 简短描述
permalink: /research/articles/your-topic/
---

研究方向详细内容...
```

#### 更新团队信息
编辑 `_data/` 目录下的 YAML 文件：
- `advisor.yml` - 导师信息
- `students.yml` - 在读学生
- `alumni.yml` - 已毕业学生

#### 添加论文
编辑 `_data/papers.yml` 文件：

```yaml
- title: "论文标题"
  authors: 作者列表
  venue: 会议/期刊名称
  year: 2024
  type: CCF-A
  doi: https://doi.org/...
```

### 4. 替换图片

#### 轮播图
替换 `assets/images/carousel/` 目录下的图片：
- slide1.jpg
- slide2.jpg
- slide3.jpg
- slide4.jpg

#### Logo
替换 `assets/images/logo.png`

#### 团队成员照片
在 `assets/images/team/` 目录下添加照片，并在对应的 YAML 文件中更新路径。

### 5. 自定义配置

编辑 `_config.yml` 文件：

```yaml
title: 实验室名称
email: lab@example.com
description: 实验室简介
address: "地址"
postal_code: "邮编"
contact_email: "联系邮箱"
```

## 样式自定义

主要样式文件：`assets/css/style.css`

可以修改的主要变量：
```css
:root {
    --primary-color: #2c3e50;      /* 主色调 */
    --secondary-color: #3498db;    /* 辅助色 */
    --accent-color: #e74c3c;       /* 强调色 */
    --container-width: 1200px;     /* 容器最大宽度 */
}
```

## 响应式设计

网站已实现响应式设计，支持：
- 桌面端（> 768px）
- 平板和移动端（≤ 768px）

## 浏览器兼容性

支持现代浏览器：
- Chrome
- Firefox
- Safari
- Edge

## 部署

### GitHub Pages
1. 在 GitHub 创建仓库
2. 推送代码到仓库
3. 在仓库设置中启用 GitHub Pages
4. 选择主分支作为部署源

### 其他部署方式
参考 Jekyll 官方文档：https://jekyllrb.com/docs/deployment/

## 技术栈

- Jekyll 4.x
- HTML5 / CSS3
- JavaScript (ES6+)
- Liquid 模板引擎

## 许可证

MIT License
