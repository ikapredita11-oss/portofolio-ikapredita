from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import os
import re

def get_video_id(url):
    pattern = r'(?:v=|/)([0-9A-Za-z_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_and_save_transcript(video_url, filename):
    video_id = get_video_id(video_url)
    if not video_id:
        print("URL tidak valid")
        return

    print(f"Mengambil transcript: {video_id}")

    try:
        # Cara baru untuk versi terbaru
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id)
        full_text = " ".join([snippet.text for snippet in fetched])

    except Exception as e:
        print(f"Error: {e}")
        return

    os.makedirs("research/youtube-transcripts", exist_ok=True)
    filepath = f"research/youtube-transcripts/{filename}.md"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# YouTube Transcript — {filename}\n\n")
        f.write(f"**URL:** {video_url}\n")
        f.write(f"**Collected:** April 2026\n\n")
        f.write("## Transcript\n\n")
        f.write(full_text)

    print(f"Tersimpan: {filepath}")

# Ganti URL dan filename di sini
video_url = "https://www.youtube.com/watch?v=SWGKLk34t7Y"
filename = "taylor-haren-12m-cold-emails-2025"

get_and_save_transcript(video_url, filename)