# 站点维护文档（ideal-wut.github.io）

本仓库为基于 Jekyll 的静态网站。本文档说明站点结构、内容维护方法、如何新增内容，以及本地预览与发布流程。文档面向日常维护和扩展使用者。

## 站点结构概览
- `_layouts/`：页面布局模板（如 `page.html`、`post.html`、`research_article.html`）。
- `_includes/`：可复用片段（如 `header.html`、`footer.html`）。
- `_posts/`：博客文章（文件名形如 `YYYY-MM-DD-title.md`）。
- `_research_articles/`：研究方向与文章介绍页面（Markdown 文件）。
- `_data/`：结构化数据（团队、校友等），如 `students.yml`、`alumni.yml`、`advisor.yml`。当前学术成果页不再使用 `papers.yml`。
- `achievements/index.html`：学术成果（论文）页面。
- `assets/`：静态资源（CSS/JS/Images）。
- 其他页面：`index.markdown`（首页）、`about.markdown`（关于）、`blog/index.html`（博客索引）、`research/index.html`（研究索引）、`joinus.md`（加入我们）、`team/index.html`（团队）。

---

## 学术成果页面维护（论文）
- 数据源：`_data/papers.yml`（结构化 YAML）。
- 渲染方式：`achievements/index.html` 从 `site.data.papers` 读取数据，支持年份筛选与分页展示。
- 更新来源：根目录的 `paper.txt` 可作为“原始清单”，通过脚本自动转换到数据源。

### 更新流程（推荐）
1. 编辑根目录 `paper.txt`，保持每条目 2-3 行、条目之间空行：
   - 第 1 行：作者；第 2 行：标题；第 3 行：期刊/会议卷期与页码 + 年份（例如：`Proc. VLDB Endow. 18(7): 2268-2280 (2025)`，或 `ICDE 2025: 4053-4065`）。
2. 运行转换脚本生成数据源：
   - 命令：`python3 scripts/paper_to_yaml.py`
   - 输出：`_data/papers.yml`（自动解析作者、标题、venue、year、pages，若存在 URL 自动作为 `doi`）。
3. 本地预览并检查：`bundle exec jekyll serve`，在浏览器访问并确认展示与筛选。

### YAML 字段约定
- `title`：论文标题。
- `authors`：作者列表（逗号分隔）。
- `venue`：会议或期刊名（不含年份，脚本会去重处理）。
- `volume_issue_pages`：卷/期/页（如存在）。
- `year`：年份（整数）。
- `doi`：第一条出现的 URL（如存在），用于“查看论文”链接。

### 常见注意事项
- `paper.txt` 中页码如 `2077-2089` 不会被误识别为年份；年份优先从 `ICDE 2023: ...` 模式或尾部括号中提取。
- 如需手工维护 `_data/papers.yml`，遵循上述字段约定；页面仅使用 `title`、`authors`、`venue`、`year`、可选 `doi`。
- 年份筛选下拉框为固定列表（2020-2025），如需扩展，请在 `achievements/index.html` 的下拉选项中增加对应年份。


---

## 博客文章维护
- 位置：`_posts/`。
- 文件命名：`YYYY-MM-DD-title.md`（如 `2025-01-15-welcome.md`）。
- 基本 Front Matter：
```yaml
---
layout: post
title: 标题
date: YYYY-MM-DD
---
```
- 正文使用 Markdown；图片请放在 `assets/images/` 并用相对路径引用。

## 研究文章维护
- 位置：`_research_articles/`。
- 基本 Front Matter（示例）：
```yaml
---
layout: research_article
title: 研究主题标题
date: YYYY-MM-DD
---
```
- 正文为 Markdown；必要时在 `assets/images/` 存放插图。

## 团队与校友维护
- 位置：`_data/` 下的 `students.yml`、`alumni.yml`、`advisor.yml`。
- 建议字段（示例）：
```yaml
- name: 张三
  role: PhD Student
  homepage: https://example.com
  email: zhangsan@example.com
  photo: /assets/images/zhangsan.jpg
```
- 页面：`team/index.html` 通常会读取数据文件进行渲染（若需调整展示，改该页面的模板逻辑）。

## 首页与导航
- 首页：`index.markdown`（可直接调整文案与模块介绍）。
- 导航与页脚：`_includes/header.html`、`_includes/footer.html`（需要全站统一变更时修改）。

## 静态资源使用
- 图片：`assets/images/`。
- 样式：`assets/css/style.css`（全站样式）。
- 脚本：`assets/js/main.js`。
- 引用图片示例：`![说明文字](/assets/images/logo.png)`。

---

## 本地预览与发布
- 环境：需要 Ruby 与 Bundler。
- 安装依赖：
```bash
bundle install
```
- 启动本地服务：
```bash
bundle exec jekyll serve
```
- 访问：`http://127.0.0.1:4000/` 或 `http://localhost:4000/`。
- 发布：推送到 GitHub 仓库（通常是 `main` 分支）后，GitHub Pages 自动构建与部署。

## 常见问题与排查
- `paper.txt` 未更新到页面：
  - 确认编辑的是根目录下的 `paper.txt`。
  - 本地服务可能缓存，重启 `jekyll serve` 或清理 `.jekyll-cache/`。
- `include_relative` 路径问题：
  - 在 `achievements/index.html` 中使用 `../paper.txt`（相对于该页面所在目录）。
- 样式问题：
  - 学术成果页使用了内联样式（`white-space: pre-line`）保持文本换行；如需更细致的样式，请在 `assets/css/style.css` 中添加新规则并移除页面内联样式。

## 内容书写风格建议
- 保持卷期页码与年份格式统一，如：`Proc. VLDB Endow. 18(7): 2268-2280 (2025)`。
- 作者列表使用英文逗号分隔；标题尽量使用官方大小写。
- 链接优先使用 DOI 或出版方页面；若有 PDF，使用 `[PDF](链接)` 形式。

---

如需新增页面或模块：
- 在根目录创建新的 Markdown/HTML 文件，并在 Front Matter 指定 `layout`。
- 复杂模块建议新建 `_layouts/` 模板或 `_includes/` 片段，以保持结构清晰。