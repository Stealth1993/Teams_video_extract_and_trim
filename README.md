# 📥 Teams Meeting Video Downloader & Cleaner

Easily download and trim Microsoft Teams meeting recordings using **FFmpeg** and **Python**.

---

## 📌 Features
✅ Download Teams meeting videos from SharePoint using FFmpeg.  
✅ Trim videos to specific timestamps using Python.  
✅ Maintain original video quality with minimal effort.  

---

## 📂 Step 1: Download the Teams Meeting Video

### 🔹 Get the Video URL from SharePoint
1. Open the **Teams recorded meeting** video in **SharePoint**.
2. Press `Ctrl + Shift + C` (to open DevTools Inspector in Chrome/Edge).
3. Go to the **Networking** tab and type **"videomanifest"** in the filter box.
4. Press `F5` to refresh the page.
5. Copy the **URL** from the results.

### 🔹 Download Using FFmpeg
Run the following command in **PowerShell**, replacing `URL` with the copied link (keep the quotes):
```powershell
ffmpeg -i "URL" -codec copy downloaded_video.mp4
```
🔗 **For more details, check:** [How to Download Teams Video](https://www.lisenet.com/2022/how-to-download-view-only-teams-meeting-recording-video-from-sharepoint/)

---

## ✂️ Step 2: Trim Video Using Python

### 🔹 Install Required Package
If you haven't installed `moviepy`, install it first:
```bash
pip install moviepy
```

### 🔹 Trim Video Using Python Script
```python
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Syntax: ffmpeg_extract_subclip("input.mp4", start_time, end_time, targetname="output.mp4")
ffmpeg_extract_subclip("downloaded_video.mp4", 60, 300, targetname="trimmed_video.mp4")
```
📌 This will extract a clip from **1 min (60s) to 5 min (300s)**.

---

## 🛠 Requirements
✔ **FFmpeg** (Download: [ffmpeg.org](https://ffmpeg.org/download.html))  
✔ **Python 3+**  
✔ **moviepy Library** (`pip install moviepy`)

---

## 🚀 Usage Example
1. Download the Teams meeting video using **FFmpeg**.
2. Trim the required portion using the **Python script**.
3. Use the trimmed video for sharing or analysis.

---

## 💡 Contributing
Feel free to fork and contribute improvements to this project!

---

## 📜 License
This project is licensed under the **MIT License**.

---

Happy coding! 🎥🚀

