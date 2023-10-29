from tkinter import Tk, Label, Radiobutton, StringVar, Entry, Button, Frame
import os
import subprocess
import yt_dlp

def create_first_window():
    first_window = Tk()
    first_window.title("Choose your download option:")
    first_window.geometry("400x220")

    separator = Frame(first_window, height=20, bg="")
    separator.pack()


    label = Label(first_window, text="Put your URL:")
    label.pack()

    separator = Frame(first_window, height=5, bg="")
    separator.pack()

    entry = Entry(first_window)
    entry.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    var = StringVar(value="option1")

    option1 = Radiobutton(first_window, text="Download Video", variable=var, value="option1")
    option1.pack()

    option2 = Radiobutton(first_window, text="Download Video and Subtitle", variable=var, value="option2")
    option2.pack()

    option3 = Radiobutton(first_window, text="Download Audio", variable=var, value="option3")
    option3.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    def submit_function():
        
        dir_output = os.path.join(os.path.join(os.path.expanduser('~')), 'YTDownloader/')
        
        data = entry.get()

        if(var.get() == "option3"):
            audio_output= dir_output+"/audio_converter"
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': audio_output,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'aac',
                    'preferredquality': '192',
                }],
            }

            # Create the yt_dlp downloader object and start the download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([data])

        else:                    

            ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': dir_output+'%(title)s.%(ext)s',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([data])
            
            
            if(var.get() == "option2"):
                file = dir_output+os.listdir(dir_output)[0]
                subprocess.run(['whisper', file, '--model','base', '--output_dir', dir_output, '--output_format', 'srt', '--language', 'English', '--fp16', 'False'],check=True)
        
        first_window.destroy()

    submit_button = Button(first_window, text="Submit", command=submit_function)
    submit_button.pack()

    first_window.mainloop()

create_first_window()