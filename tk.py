""" from tkinter import *

def change_window():
    window.destroy()
    new_window = Tk()
    new_window.title("New Window")
    new_window.geometry("200x200")
    new_window.mainloop()

options = ["Option 1", "Option 2", "Option 3"]

window = Tk()
window.title("Window")
window.geometry("200x200")

optVariable = StringVar(window)
optVariable.set(options[0])

optMenu = OptionMenu(window, optVariable, *options)
optMenu.pack()

button = Button(window, text="Change Window", command=change_window)
button.pack()

window.mainloop() """

from tkinter import *
import yt_dlp
import tkinter
import subprocess
import os
import webbrowser


def change_window():
    window.destroy()
    if(var.get()=="btn1"): option1()

url = ''
# https://www.youtube.com/watch?v=1aA1WGON49E&t=16s

def submit(input_box):
    global url
    url = input_box
    print("url")

def option1():
    window = Tk()
    separator = Frame(window, height=10, bg="")
    separator.pack(fill=X, padx=5, pady=5)
    label = Label(window, text="Put your URL:")
    window.geometry("400x200")
    label.pack()
    input_box = Entry(window)
    input_box.pack()
    separator = Frame(window, height=10, bg="")
    separator.pack(fill=X, padx=5, pady=5)
    submit_button = Button(window, text="Submit")
    submit_button.pack()

    dir_output = os.path.join(os.path.join(os.path.expanduser('~')), 'Videos/YoutubeDownloader/')
""" 
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': dir_output+'%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    window.geometry("400x200")
    window.mainloop() """

window = Tk()
window.title("Youtube Downloader")
window.geometry("400x200")

separator = Frame(window, height=10, bg="")
separator.pack(fill=X, padx=5, pady=5)

label = Label(window, text="Choose your download option:")
label.pack()

separator = Frame(window, height=5, bg="")
separator.pack(fill=X, padx=5, pady=5)

var = StringVar()
var.set("Youtube Video")

rb1 = Radiobutton(window, text="Youtube Video", variable=var, value="btn1")
rb1.pack()

rb2 = Radiobutton(window, text="Youtube Video with subtitles", variable=var, value="btn2")
rb2.pack()

rb3 = Radiobutton(window, text="Subtitles from Video", variable=var, value="btn3")
rb3.pack()

separator = Frame(window, height=5, bg="")
separator.pack(fill=X, padx=5, pady=5)

button = Button(window, text="Run Window", command=change_window)
button.pack()

window.mainloop()