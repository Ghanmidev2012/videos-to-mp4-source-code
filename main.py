import yt_dlp

def download_youtube_video(video_url):
    print("starting installing")

    yt_opts = {
    'format': 'best[ext=mp4]',
    'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download([video_url])
        print("finish to transform to mp4")
    except Exception as e:
        print(f"the are error in installation : {e}")
if __name__ == "__main__":
    url = input("enter url of video:").strip()

    if url:
        download_youtube_video(url)








    
