# 快速上手指南

## 第一步：安装依赖

确保已安装 Ruby 和 Bundler，然后运行：

```bash
bundle install
```

## 第二步：本地预览

```bash
bundle exec jekyll serve
```

在浏览器中访问 `http://localhost:4000`

## 第三步：自定义网站内容

### 1. 修改基本信息

编辑 `_config.yml`：

```yaml
title: 你的实验室名称
email: your-lab@example.com
description: 实验室简介描述
address: "实验室地址"
postal_code: "邮政编码"
contact_email: "联系邮箱"
```

### 2. 添加图片

#### 轮播图
将4张图片放到 `assets/images/carousel/` 目录：
- slide1.jpg
- slide2.jpg
- slide3.jpg
- slide4.jpg

#### Logo
将 logo 文件保存为 `assets/images/logo.png`

#### 默认头像
将默认头像保存为 `assets/images/default-avatar.jpg`

### 3. 更新导师信息

编辑 `_data/advisor.yml`：

```yaml
name: 导师姓名
title: 职称
email: 邮箱
office: 办公室
phone: 电话
avatar: /assets/images/team/advisor.jpg
bio: |
  导师简介...
research_interests:
  - 研究兴趣1
  - 研究兴趣2
```

### 4. 添加学生信息

编辑 `_data/students.yml`：

```yaml
- name: 学生姓名
  year: 2025
  research: 研究方向
  avatar: /assets/images/team/student1.jpg
```

编辑 `_data/alumni.yml`：

```yaml
- name: 姓名
  graduationYear: 2024
  paper: 论文题目
  employment: 就业去向
  avatar: /assets/images/team/alumni1.jpg
```

### 5. 添加论文

编辑 `_data/papers.yml`：

```yaml
- title: "论文标题"
  authors: 作者列表
  venue: 会议/期刊
  year: 2024
  type: CCF-A  # 或 CCF-B, CCF-C
  doi: https://doi.org/...
```

### 6. 发布博客文章

在 `_posts/` 目录创建文件 `YYYY-MM-DD-title.md`：

```markdown
---
layout: post
title: "文章标题"
date: 2025-01-15
author: 作者
---

文章内容...
```

### 7. 修改首页介绍

编辑 `index.markdown`，修改实验室简介内容。

### 8. 自定义研究方向

编辑 `_research_articles/` 目录下的三个文件：
- `time-series.md` - 时序数据分析
- `spatio-temporal.md` - 时空数据挖掘
- `vector-search.md` - 向量检索

或创建新的研究方向文章。

### 9. 修改"加入我们"页面

编辑 `joinus.md`，更新招生信息和要求。

## 第四步：测试网站

访问以下页面确保一切正常：

- [x] 首页：`http://localhost:4000/`
- [x] 动态：`http://localhost:4000/blog/`
- [x] 研究方向：`http://localhost:4000/research/`
- [x] 指导教师：`http://localhost:4000/team/`
- [x] 在读学生：`http://localhost:4000/team/students/`
- [x] 已毕业学生：`http://localhost:4000/team/alumni/`
- [x] 研究成果：`http://localhost:4000/achievements/`
- [x] 加入我们：`http://localhost:4000/joinus/`

## 第五步：部署到 GitHub Pages

1. 创建 GitHub 仓库
2. 推送代码：

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/yourrepo.git
git push -u origin main
```

3. 在 GitHub 仓库设置中启用 Pages
4. 选择 main 分支作为源
5. 访问 `https://yourusername.github.io/yourrepo/`

## 常见问题

### Q: 轮播图不显示？
A: 确保在 `assets/images/carousel/` 目录下有 slide1.jpg 到 slide4.jpg 四张图片。

### Q: 团队成员头像显示默认图片？
A: 检查图片路径是否正确，确保图片文件存在。

### Q: 论文筛选不工作？
A: 确保 `_data/papers.yml` 中的 year 和 type 字段格式正确。

### Q: 修改配置后网站没有更新？
A: 修改 `_config.yml` 后需要重启 Jekyll 服务器（Ctrl+C 然后重新运行 `bundle exec jekyll serve`）。

## 进阶自定义

### 修改颜色主题

编辑 `assets/css/style.css` 中的 CSS 变量：

```css
:root {
    --primary-color: #2c3e50;      /* 主色调 */
    --secondary-color: #3498db;    /* 链接颜色 */
    --accent-color: #e74c3c;       /* 强调色 */
}
```

### 添加新的导航项

编辑 `_config.yml` 的 navigation 部分：

```yaml
navigation:
  - title: 新页面
    url: /newpage/
```

然后创建对应的页面文件。

## 需要帮助？

- Jekyll 官方文档：https://jekyllrb.com/docs/
- Liquid 模板文档：https://shopify.github.io/liquid/
- 查看 `README.md` 获取更详细的文档

祝你使用愉快！
