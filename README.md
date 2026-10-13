# 软件官网 · 一键直达

> 一个纯静态的「常用软件官网导航」页面。点击图标，直达官方站点。
> 国内 / 国外分组，支持关键词搜索、深色模式。

<p>
  <img alt="status" src="https://img.shields.io/badge/status-online-3ecf8e?style=flat-square">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-3b6cf6?style=flat-square">
  <img alt="build" src="https://img.shields.io/badge/build-none%20required-79808f?style=flat-square">
  <img alt="apps" src="https://img.shields.io/badge/entries-16-e5484d?style=flat-square">
</p>

**线上地址：** <https://bury-hui.github.io/Official-Site/>

---

## 这是什么

日常上网时，找某个软件的**官方网站**往往要在搜索结果里翻半天——广告、山寨站、第三方下载站混在一起。这个项目把常用软件的官方入口整理成一页，点一下就到，不用再搜。

它由两部分组成，共用同一份页面：

| 形态 | 说明 |
| --- | --- |
| **网页版** | 打开即用，无需安装。手机、电脑浏览器都能访问 |
| **安卓 App** | 把同一个页面封装进 WebView，桌面上有一个图标，点开就是这页 |

页面本身是**单文件** `index.html`，不依赖任何框架、构建工具或 CDN。图标是本地资源，断网也能打开（点链接时除外）。

---

## 收录清单

一共 **16 个**入口，按「国内 / 国外」分成两组。

### 国内软件

| 图标 | 名称 | 说明 | 官网 |
| --- | --- | --- | --- |
| <img src="icons/doubao.png" width="20"> | 豆包 | 字节跳动 AI 助手 | <https://www.doubao.com/> |
| <img src="icons/deepseek.ico" width="20"> | DeepSeek | 深度求索 | <https://www.deepseek.com/> |
| <img src="icons/qianwen.png" width="20"> | 千问 | 阿里巴巴 | <https://www.qianwen.com/> |
| <img src="icons/mimo.png" width="20"> | 小米 MiMo | Xiaomi MiMo | <https://mimo.mi.com/> |
| <img src="icons/kimi.png" width="20"> | Kimi | 月之暗面 | <https://www.kimi.com/> |
| <img src="icons/workbuddy.svg" width="20"> | WorkBuddy | AI 工作助手 | <https://www.workbuddy.cn/app> |
| <img src="icons/kanju.png" width="20"> | 看剧 AI | Kanju AI | <https://kanju1.ai/> |

### 国外软件

| 图标 | 名称 | 说明 | 官网 |
| --- | --- | --- | --- |
| <img src="icons/github.svg" width="20"> | GitHub | 代码托管平台 | <https://github.com/> |
| <img src="icons/chatgpt.svg" width="20"> | ChatGPT | OpenAI | <https://chatgpt.com/> |
| <img src="icons/tiktok.svg" width="20"> | TikTok | 短视频平台 | <https://www.tiktok.com/> |
| <img src="icons/x.svg" width="20"> | X | 推特 | <https://x.com/> |
| <img src="icons/youtube.svg" width="20"> | YouTube | 视频平台 | <https://www.youtube.com/> |
| <img src="icons/facebook.svg" width="20"> | Facebook | Meta | <https://www.facebook.com/> |
| <img src="icons/telegram.svg" width="20"> | Telegram | 即时通讯 | <https://telegram.org/> |
| <img src="icons/instagram.svg" width="20"> | Instagram | Meta | <https://www.instagram.com/> |
| <img src="icons/whatsapp.svg" width="20"> | WhatsApp | Meta | <https://www.whatsapp.com/> |

---

## 功能

- **一键直达** — 卡片即链接，点击在新标签页打开官网，避免误入山寨站。
- **关键词搜索** — 顶部搜索框支持按中文名、英文名、网址模糊匹配，输入即时过滤。
- **分组切换** — 底部导航栏可在「全部 / 国内软件 / 国外软件」之间切换。桌面端是浮动胶囊，移动端是贴底 Tab 栏。
- **深色模式** — 右上角按钮切换，选择会记在浏览器里，下次打开保持一致。
- **键盘快捷键** — 按 `/` 聚焦搜索框，按 `Esc` 清空并退出。
- **自适应布局** — 桌面端多列网格，手机端自动收窄为两列以上，图标等比缩放。
- **响应式动效** — 卡片悬浮上浮、图标微旋，进入页面时逐张升起；均为纯 CSS，无动画库。
- **App 内增强** — 检测到运行在 App 的 WebView 中时，自动去掉 `target="_blank"`，改由宿主调用系统浏览器打开链接，并同步深色主题状态。

---

## 项目结构

```
.
├── index.html          # 全部内容：结构 + 样式 + 数据 + 逻辑（单文件）
├── icons/              # 16 个软件图标（png / svg / ico）
│   ├── doubao.png
│   ├── deepseek.ico
│   ├── qianwen.png
│   ├── mimo.png
│   ├── kimi.png
│   ├── workbuddy.svg
│   ├── kanju.png
│   ├── github.svg
│   ├── chatgpt.svg
│   ├── tiktok.svg
│   ├── x.svg
│   ├── youtube.svg
│   ├── facebook.svg
│   ├── telegram.svg
│   ├── instagram.svg
│   └── whatsapp.svg
└── .nojekyll            # 告诉 GitHub Pages 跳过 Jekyll 处理
```

整个站点总计约 **380 KB**，最大的一块是图标资源。没有任何依赖需要安装。

---

## 部署

### 在线访问

已通过 **GitHub Pages** 发布，源为 `main` 分支根目录：

<https://bury-hui.github.io/Official-Site/>

推送到 `main` 分支后，Pages 会自动重新构建，通常一分钟内生效。

### 本地预览

`index.html` 双击就能打开。如果想让 `file://` 之外的相对路径行为更接近线上，也可以用任意静态服务器：

```bash
# 任选其一，在项目根目录执行
python -m http.server 8080
npx serve .
```

然后访问 <http://127.0.0.1:8080/>。

---

## 修改内容

所有软件条目集中在 `index.html` 里的 `APPS` 数组，一条一行：

```js
const APPS = [
  /* ---------- 国内 ---------- */
  { name:"豆包",      en:"Doubao",     url:"https://www.doubao.com/",  icon:"icons/doubao.png",  group:"cn" },
  { name:"小米 MiMo", en:"Xiaomi MiMo", url:"https://mimo.mi.com/",    icon:"icons/mimo.png",    group:"cn" },
  /* ---------- 国外 ---------- */
  { name:"GitHub",    en:"代码托管平台", url:"https://github.com/",     icon:"icons/github.svg",  group:"intl", mono:true }
];
```

**字段说明：**

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `name` | 是 | 卡片主标题（中文名） |
| `en` | 是 | 卡片副标题，一般放英文名或公司名 |
| `url` | 是 | 官网地址，点击后跳转 |
| `icon` | 是 | 图标路径，相对于 `index.html` |
| `group` | 是 | `"cn"` 国内 / `"intl"` 国外 |
| `mono` | 否 | `true` 表示单色图标，深色模式下自动反色 |
| `iconBg` | 否 | 覆盖图标底色，例如 `"#000000"`，适合纯黑底的品牌图标 |

### 新增一个软件

1. 把图标文件放进 `icons/` 目录。
2. 在 `APPS` 数组对应分组里加一行。
3. 保存，刷新页面即可看到——**无需重启、无需构建**。

如果新图标是纯黑或纯白的单色 SVG，记得加上 `"mono": true`，否则深色模式下会看不清。

---

## 技术说明

- 纯客户端实现，**没有后端**，不收集任何用户数据，不写入 Cookie。
- 主题偏好通过 `localStorage` 保存在本地，读取时用 `try/catch` 包裹，隐私模式下也不会报错。
- 样式全部走 CSS 自定义属性（`--bg`、`--card`、`--text` 等），深色模式只切换 `html[data-theme="dark"]` 下的变量值，切换时不会闪白。
- 无第三方脚本、无埋点、无字体外链，页面在离线状态下（除跳转）仍可正常渲染。

---

## 许可与致谢

- 页面代码以 **MIT** 许可开放，可自由取用、修改。
- 各软件**图标与商标版权归各自品牌所有**，此处仅用于导航指向，不构成任何形式的授权或背书。
- 收录对象均为对应产品的官方站点，不含第三方下载站或镜像站。

---

<p align="center">
  <sub>如果这个页面帮你少搜了几次，欢迎点个 Star ⭐</sub>
</p>
