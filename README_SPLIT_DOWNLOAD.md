# SLAM 网页简历分包说明

把所有 `web_resume_slam_part_*.zip` 下载到同一个文件夹后，依次解压到同一个位置。解压完成后，你会得到 `web_resume_project_slam/` 文件夹。

解压全部分包后，运行：

```bash
cd web_resume_project_slam
python merge_project_parts.py
```

然后双击打开 `index.html` 即可。

Windows 用户也可以在 `web_resume_project_slam` 文件夹中按住 Shift + 右键，选择“在终端中打开”，再执行：

```powershell
python merge_project_parts.py
```

如果电脑没有 Python，也可以手动合并两个被拆分的大文件：

```bash
cat assets/_split_parts/f2-19-map-compare.png.part-* > assets/f2-19-map-compare.png
cat assets/_split_parts/locate-slam.mp4.part-* > assets/videos/locate-slam.mp4
```

Windows PowerShell 手动合并命令：

```powershell
cmd /c copy /b assets\_split_parts\f2-19-map-compare.png.part-* assets\f2-19-map-compare.png
cmd /c copy /b assets\_split_parts\locate-slam.mp4.part-* assets\videos\locate-slam.mp4
```
