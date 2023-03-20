import subprocess
import os
import webbrowser
import tkinter
import yt_dlp

url = ''
# https://www.youtube.com/watch?v=1aA1WGON49E&t=16s

def submit():
    global url
    url = input_box.get()
    window.destroy()


window = tkinter.Tk()
window.geometry("300x150")
label = tkinter.Label(window, text="Put your URL:")
label.pack()
input_box = tkinter.Entry(window)
input_box.pack()
submit_button = tkinter.Button(window, text="Submit", command=submit)
submit_button.pack()
window.mainloop()

dir_output = os.path.join(os.path.join(os.path.expanduser('~')), 'Videos/YoutubeDownloader/')

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': dir_output+'%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

file = dir_output+os.listdir(dir_output)[0]

subprocess.run(['whisper', file, '--model','base', '--output_dir', dir_output, '--output_format', 'srt'],check=True)
webbrowser.open(os.path.realpath(dir_output))