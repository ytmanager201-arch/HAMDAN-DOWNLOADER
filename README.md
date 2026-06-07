🚀 HAMDAN DOWNLOADER PRO
HAMDAN DOWNLOADER is a high-performance, professional-grade desktop application for downloading videos, reels, posts, and profiles from YouTube, Instagram, TikTok, Facebook, and 1000+ other platforms. Built with a beautiful dark-themed UI, real-time live progress tracking, and 10x speed boost technology.

VersionPythonLicense

✨ Features
🎬 Multi-Platform Support
YouTube: Single video, Bulk links, Full Channel, and Playlist downloading with optional Thumbnail save.
Instagram: Single Post/Reel download, Full Profile scanner (downloads all posts & reels).
TikTok / Facebook: Single video (No Watermark for TikTok), Full Profile/Page scanner.
Universal Bulk: Paste multiple URLs from any platform at once, fetch details with previews, and download.

⚡ Advanced Backend Engine
10x Speed Boost: Uses concurrent_fragment_downloads to download video fragments in parallel.
Auto-Update System: One-click yt-dlp engine update directly from the UI.
Real-Time Live Progress: Powered by Flask-SocketIO, see exact download percentage, speed (MB/s), and ETA live on screen.
Auto Port Detection: Dynamically finds a free port, so you never get "Port already in use" errors.

🍪 Advanced Cookie Manager
Save cookies locally for YouTube, Instagram, TikTok, and Facebook.
Fixes downloading errors for private/restricted content and Instagram profiles.
Import cookies easily using browser extensions (Netscape format).

🖥️ Standalone Desktop App
Runs in its own native window using pywebview (No browser tabs needed!).
Clean, modern, and crystal-clear UI/UX with the signature "Hamdan Green" accent.
Closing the window safely kills the background server.

📸 Screenshots
(Add your app screenshots here by dragging and dropping images into this README on GitHub)

[Dashboard Screenshot][YouTube Downloader Screenshot][Live Progress Screenshot]

🛠️ Tech Stack
Frontend: HTML5, CSS3, Vanilla JavaScript, Socket.IO Client, Font Awesome
Backend: Python, Flask, Flask-SocketIO
Core Engine: yt-dlp
Desktop Window: pywebview
Build Tool: PyInstaller

🚀 Getting Started (Run from Source)
Prerequisites
Python 3.10 or higher installed on your PC.
pip (Package installer for Python).
Installation
Clone the repository
git clone https://github.com/your-username/HAMDAN-DOWNLOADER.gitcd HAMDAN-DOWNLOADER

Install dependencies
pip install -r requirements.txt

Run the application
python main.py

🍪 How to Get Cookies (For Instagram/Private Content)
To download private content or Instagram profiles, cookies are required:

Install the "Get cookies.txt LOCALLY" extension in your Chrome/Firefox browser.
Log into the respective platform (e.g., Instagram) in your browser.
Click the extension and Export the cookies.
Open the downloaded .txt file, copy all the text.
Paste it in the Settings & Cookies tab of HAMDAN DOWNLOADER and click Save Cookies.

👤 Author & Contact
Kashoo Khan

📘 Facebook: Kashoo Khan
Feel free to reach out for support, collaborations, or custom software development!

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

⭐ If you like this project, don't forget to give it a star on GitHub! ⭐
