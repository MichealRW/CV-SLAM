# 王硕 · SLAM 求职网页简历

这是一个可直接部署到 **GitHub Pages** 的纯静态网页简历项目，聚焦以下求职方向：

- SLAM / 多传感融合定位
- 机器人感知 / 三维建图
- 长期地图维护
- 变化检测与地图更新
- 动态环境感知

## 项目结构

```text
web_resume_project_slam/
├── index.html
├── favicon.svg
├── README.md
└── assets/
    ├── *.png / *.webp
    └── videos/
        ├── locate-slam.mp4
        └── PGP-DOR.mp4
```

## 部署方式

### 方式一：直接本地打开
双击 `index.html` 即可预览。

### 方式二：部署到 GitHub Pages
1. 新建一个 GitHub 仓库。
2. 把当前目录下所有文件上传到仓库根目录。
3. 进入 `Settings -> Pages`。
4. 在 `Build and deployment` 中选择：
   - `Source`: `Deploy from a branch`
   - `Branch`: `main`
   - `Folder`: `/(root)`
5. 保存后等待几分钟，即可通过 Pages 链接访问。

## 使用说明

- 页面已内嵌图片与视频演示，适合直接作为求职链接发送。
- 所有路径均为相对路径，适合 GitHub Pages 项目页部署。
- 如果后续还要补充论文链接、PDF 简历、发表成果或竞赛经历，可直接在 `index.html` 中继续扩展对应区块。
