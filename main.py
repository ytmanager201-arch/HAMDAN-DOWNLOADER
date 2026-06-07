import os
import sys
import threading
import subprocess
import yt_dlp
import webbrowser
from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# --- PATHS SETUP ---
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.abspath(".")

DOWNLOAD_DIR = os.path.join(os.path.expanduser('~'), 'Downloads', 'HAMDAN-DOWNLOADER')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

COOKIE_DIR = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'HAMDAN-DOWNLOADER', 'cookies')
os.makedirs(COOKIE_DIR, exist_ok=True)

def get_cookie_path(platform):
    return os.path.join(COOKIE_DIR, f'{platform}_cookies.txt')

# --- SERVE FRONTEND ---
@app.route('/')
def serve_index():
    return send_from_directory(BASE_DIR, 'index.html')

# --- YT-DLP UPDATE ---
@app.route('/api/update-ytdlp', methods=['GET'])
def update_ytdlp():
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'yt-dlp'], capture_output=True, text=True)
        if "Successfully installed" in result.stdout or "Requirement already satisfied" in result.stdout:
            return jsonify({'success': True, 'message': 'yt-dlp updated!'})
        return jsonify({'success': False, 'error': result.stdout})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# --- FETCH INFO ---
@app.route('/api/fetch-info', methods=['POST'])
def fetch_info():
    data = request.json
    url = data.get('url', '')
    platform = data.get('platform', 'other')
    
    cookie_file = get_cookie_path(platform)
    if not os.path.exists(cookie_file): cookie_file = None

    is_playlist = any(x in url for x in ['playlist', '/channels/', '/c/', '/@', 'instagram.com/', 'tiktok.com/@'])
    
    ydl_opts = {
        'quiet': True, 'no_warnings': True, 'skip_download': True,
        'cookiefile': cookie_file, 'no_check_certificates': True,
        'extract_flat': 'in_playlist' if is_playlist else False, 'playlistend': 50,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                items = []
                for entry in info.get('entries', [])[:50]:
                    if entry:
                        items.append({
                            'title': entry.get('title', 'Untitled'),
                            'thumbnail': entry.get('thumbnail', '') or 'https://picsum.photos/seed/def/320/180',
                            'url': entry.get('url') or entry.get('webpage_url'),
                            'duration': entry.get('duration_string', 'N/A')
                        })
                return jsonify({'success': True, 'type': 'list', 'data': {'title': info.get('title', 'Profile/Playlist'), 'items': items}})
            
            filesize_approx = info.get('filesize') or info.get('filesize_approx')
            filesize_mb = f"{round(filesize_approx / (1024 * 1024), 2)} MB" if filesize_approx else "N/A"

            result = {
                'title': info.get('title', 'Unknown Title'),
                'thumbnail': info.get('thumbnail', '') or 'https://picsum.photos/seed/def/320/180',
                'duration': info.get('duration_string', '0:00'),
                'uploader': info.get('uploader', 'Unknown'),
                'filesize': filesize_mb, 'url': url
            }
            return jsonify({'success': True, 'type': 'single', 'data': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# --- REAL-TIME PROGRESS HOOK ---
def ytdlp_progress_hook(d, task_id):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        
        # Frontend ko real-time data bhejo
        socketio.emit('download_progress', {
            'task_id': task_id,
            'percent': percent,
            'speed': speed,
            'eta': eta
        })
    elif d['status'] == 'finished':
        socketio.emit('download_progress', {
            'task_id': task_id,
            'percent': '100%',
            'speed': 'N/A',
            'eta': 'Done!'
        })

# --- START DOWNLOAD ---
@app.route('/api/download', methods=['POST'])
def start_download():
    data = request.json
    urls = data.get('urls', [])
    quality = data.get('quality', 'best')
    platform = data.get('platform', 'other')
    download_thumb = data.get('download_thumbnail', False)
    task_id = data.get('task_id', 'task-unknown') # Frontend se unique ID aayegi

    cookie_file = get_cookie_path(platform)
    if not os.path.exists(cookie_file): cookie_file = None

    if not urls: return jsonify({'success': False, 'error': 'No URLs'})

    # Har URL ke liye naya thread
    for url in urls:
        thread = threading.Thread(target=download_video, args=(url, quality, platform, cookie_file, download_thumb, task_id))
        thread.start()
    
    return jsonify({'success': True, 'message': 'Download Started!'})

def download_video(url, quality, platform, cookie_file, download_thumb, task_id):
    if quality == 'mp3' or quality == 'm4a':
        format_opt = 'bestaudio/best'
        postprocessors = [{'key': 'FFmpegExtractAudioPP', 'preferredcodec': quality}]
    elif quality == 'best':
        format_opt = 'bestvideo+bestaudio/best'
        postprocessors = []
    else:
        format_opt = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'
        postprocessors = []

    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
        'format': format_opt,
        'cookiefile': cookie_file,
        'no_check_certificates': True,
        'postprocessors': postprocessors,
        'merge_output_format': 'mp4',
        'concurrent_fragment_downloads': 10, 
        'write_thumbnail': download_thumb,
        'writethumbnail': download_thumb,
        'progress_hooks': [lambda d: ytdlp_progress_hook(d, task_id)], # Real-time hook
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        socketio.emit('download_progress', {'task_id': task_id, 'percent': 'ERR', 'speed': 'Failed', 'eta': str(e)[:50]})

# --- COOKIES MANAGEMENT ---
@app.route('/api/save-cookies', methods=['POST'])
def save_cookies():
    data = request.json
    platform = data.get('platform', '').lower()
    cookie_string = data.get('cookie_string', '')
    if not platform or not cookie_string: return jsonify({'success': False, 'error': 'Missing data'})
    cookie_file = get_cookie_path(platform)
    with open(cookie_file, 'w', encoding='utf-8') as f:
        f.write("# Netscape HTTP Cookie File\n")
        cookies = cookie_string.split(';')
        domain = f'.{platform}.com'
        for cookie in cookies:
            cookie = cookie.strip()
            if '=' in cookie:
                name, value = cookie.split('=', 1)
                f.write(f"{domain}\tTRUE\t/\tTRUE\t0\t{name.strip()}\t{value.strip()}\n")
    return jsonify({'success': True, 'message': f'{platform} Cookies Saved!'})

@app.route('/api/get-cookies-status', methods=['GET'])
def get_cookies_status():
    platforms = ['youtube', 'instagram', 'tiktok', 'facebook']
    status = {}
    for p in platforms: status[p] = os.path.exists(get_cookie_path(p))
    return jsonify({'success': True, 'status': status})

if __name__ == '__main__':
    # Auto-open browser when EXE starts
    threading.Timer(1.5, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    print("🚀 Starting HAMDAN DOWNLOADER Backend...")
    print(f"📂 Downloads: {DOWNLOAD_DIR}")
    # Use socketio.run instead of app.run
    socketio.run(app, host='127.0.0.1', port=5000, debug=False, allow_unsafe_werkzeug=True)