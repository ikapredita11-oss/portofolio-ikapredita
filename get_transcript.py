from youtube_transcript_api import YouTubeTranscriptApi
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
    transcript_list = YouTubeTranscriptApi().fetch(video_id)
    full_text_parts = []
    for item in transcript_list:
        if isinstance(item, dict):
            full_text_parts.append(item.get("text", ""))
        else:
            full_text_parts.append(getattr(item, "text", ""))
    full_text = " ".join(part for part in full_text_parts if part)
    os.makedirs("research/youtube-transcripts", exist_ok=True)
    filepath = f"research/youtube-transcripts/{filename}.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# YouTube Transcript — {filename}\n\n")
        f.write(f"**Collected:** April 2026\n\n")
        f.write("## Transcript\n\n")
        f.write(full_text)
    print(f"✅ Tersimpan: {filepath}")

# Ganti URL dan filename sesuai video yang ingin diambil
video_urls = [
    "https://youtu.be/bLCeTeTZSFU?si=JUjf2qqh8FRsrV-n"
    
    

]
filenames = [
    "taylor-haren-sent-50M-cold-emails"


    
]

if len(video_urls) != len(filenames):
    raise ValueError("Jumlah video URL dan filename harus sama.")

for video_url, filename in zip(video_urls, filenames):
    get_and_save_transcript(video_url, filename)