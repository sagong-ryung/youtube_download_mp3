# YouTube Audio Downloader for MP3

This script allows you to download audio from YouTube videos and playlists in MP3 format.

## Requirements

- Python 3
- `yt_dlp` library
- ffmpeg

Install yt_dlp

```bash
pip install yt_dlp
```

download ffmpeg

[https://github.com/BtbN/FFmpeg-Builds/releases](https://github.com/BtbN/FFmpeg-Builds/releases)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-audio-downloader.git
cd youtube_download_mp3
```

2. Modify the `main()` function in `main.py` to include the YouTube URLs you want to download.

```python
URL_LIST = [
    "https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE",
    # Add more URLs as needed
]

yd = YoutubeDowonloader()
yd.download(URL_LIST)
```

3. Run the script:

```bash
python main.py
```

The downloaded audio files will be saved in the `./result` directory.

## Configuration

You can customize the output directory and other options in the `YoutubeDowonloader` class in `main.py`. Open the script and modify the `self.ydl_opts` dictionary according to your preferences.

## Disclaimer

Make sure to comply with YouTube's terms of service when using this script. Downloading videos without permission may violate YouTube's policies.

**Note:** Ensure that you have the necessary rights to download and use the content.