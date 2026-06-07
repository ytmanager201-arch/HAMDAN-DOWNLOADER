Bhai, ye raha professional `README.md` file tumhare repository ke liye. Isme project ki poori detail, installation, EXE banane ka tareeka, aur tumhara contact info sab include hai. Isko seedha copy karke `README.md` file mein paste kar do.

---

```markdown
# 🚀 HAMDAN DOWNLOADER PRO

**HAMDAN DOWNLOADER** is a high-performance, professional-grade desktop application for downloading videos, reels, posts, and profiles from YouTube, Instagram, TikTok, Facebook, and 1000+ other platforms. Built with a beautiful dark-themed UI, real-time live progress tracking, and 10x speed boost technology.

![Version](https://img.shields.io/badge/Version-2.0-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

### 🎬 Multi-Platform Support
- **YouTube**: Single video, Bulk links, Full Channel, and Playlist downloading with optional Thumbnail save.
- **Instagram**: Single Post/Reel download, Full Profile scanner (downloads all posts & reels).
- **TikTok / Facebook**: Single video (No Watermark for TikTok), Full Profile/Page scanner.
- **Universal Bulk**: Paste multiple URLs from any platform at once, fetch details with previews, and download.

### ⚡ Advanced Backend Engine
- **10x Speed Boost**: Uses `concurrent_fragment_downloads` to download video fragments in parallel.
- **Auto-Update System**: One-click yt-dlp engine update directly from the UI.
- **Real-Time Live Progress**: Powered by `Flask-SocketIO`, see exact download percentage, speed (MB/s), and ETA live on screen.
- **Auto Port Detection**: Dynamically finds a free port, so you never get "Port already in use" errors.

### 🍪 Advanced Cookie Manager
- Save cookies locally for YouTube, Instagram, TikTok, and Facebook.
- Fixes downloading errors for private/restricted content and Instagram profiles.
- Import cookies easily using browser extensions (Netscape format).

### 🖥️ Standalone Desktop App
- Runs in its own native window using `pywebview` (No browser tabs needed!).
- Clean, modern, and crystal-clear UI/UX with the signature "Hamdan Green" accent.
- Closing the window safely kills the background server.

---

## 📸 Screenshots

*(Add your app screenshots here by dragging and dropping images into this README on GitHub)*

`[Dashboard Screenshot]`
`[YouTube Downloader Screenshot]`
`[Live Progress Screenshot]`

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript, Socket.IO Client, Font Awesome
- **Backend**: Python, Flask, Flask-SocketIO
- **Core Engine**: yt-dlp
- **Desktop Window**: pywebview
- **Build Tool**: PyInstaller

---

## 🚀 Getting Started (Run from Source)

### Prerequisites
- Python 3.10 or higher installed on your PC.
- pip (Package installer for Python).

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/HAMDAN-DOWNLOADER.git
   cd HAMDAN-DOWNLOADER
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```
   *The app will automatically open in a native desktop window!*

---

## 📦 Building the Standalone EXE

To create a single `.exe` file that you can share with anyone (they won't need Python installed):

1. **Get an Icon**: Place your icon file in the project folder and name it `hamdan.ico`.
2. **Run PyInstaller**: Open terminal in the project folder and run this exact command:

   *(For Windows CMD)*
   ```cmd
   pyinstaller --onefile --windowed --icon=hamdan.ico --add-data "index.html;." --hidden-import=engineio.async_drivers.threading --hidden-import=pywebview --name "HamdanDownloader" main.py
   ```

   *(For PowerShell or Linux/Mac)*
   ```bash
   pyinstaller --onefile --windowed --icon=hamdan.ico --add-data "index.html:." --hidden-import=engineio.async_drivers.threading --hidden-import=pywebview --name "HamdanDownloader" main.py
   ```

3. **Get your EXE**: Once the process completes, go to the `dist` folder. You will find `HamdanDownloader.exe` ready to use!

**Command Flags Explained:**
- `--onefile`: Packs everything into a single EXE.
- `--windowed`: Hides the black CMD terminal background.
- `--icon=hamdan.ico`: Sets your custom desktop icon.
- `--add-data`: Packs the HTML UI inside the EXE.
- `--hidden-import`: Ensures PyInstaller doesn't miss backend packages.

---

## 🍪 How to Get Cookies (For Instagram/Private Content)

To download private content or Instagram profiles, cookies are required:

1. Install the **"Get cookies.txt LOCALLY"** extension in your Chrome/Firefox browser.
2. Log into the respective platform (e.g., Instagram) in your browser.
3. Click the extension and **Export** the cookies.
4. Open the downloaded `.txt` file, copy all the text.
5. Paste it in the **Settings & Cookies** tab of HAMDAN DOWNLOADER and click **Save Cookies**.

---

## 👤 Author & Contact

**Kashoo Khan**

- 📘 **Facebook**: [Kashoo Khan](https://www.facebook.com/kashookhan2002)

Feel free to reach out for support, collaborations, or custom software development!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ **If you like this project, don't forget to give it a star on GitHub!** ⭐
```

---

Ye README GitHub pe bahut professional lagega. Isme badges, clear headings, installation steps, EXE build command ka explanation, aur tumhara contact info sab mast tareeke se formatted hai!
