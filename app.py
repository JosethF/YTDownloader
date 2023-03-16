import subprocess
import os
import webbrowser
import tkinter
from pytube import YouTube

# Put video URL
url = ''

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

# Download youtube video
video = YouTube(url)
video_stream = video.streams.get_highest_resolution()
video_stream.download(dir_output)

file = dir_output+os.listdir(dir_output)[0]

subprocess.run(['whisper', file, '--model','base', '--output_dir', dir_output, '--output_format', 'srt'],check=True)
webbrowser.open(os.path.realpath(dir_output))