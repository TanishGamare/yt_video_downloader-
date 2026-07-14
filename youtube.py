import yt_dlp  
import tkinter as tk 
from tkinter import filedialog 

def download_video(url, save_path):

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Video Downloaded Successfully!")

    except Exception as e:
        print(e)

def open_file_dialogue():
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")
    return folder 

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a youtube url: ")
    save_dir = open_file_dialogue()

    if save_dir:
        print("started download....")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.") 
