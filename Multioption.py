from tkinter import Tk, Label, Radiobutton, StringVar, Entry, Button, Frame, filedialog
import os
import subprocess
import yt_dlp

def create_first_window():
    first_window = Tk()
    first_window.title("Choose your download option:")
    first_window.geometry("400x200")

    input_file = ''

    separator = Frame(first_window, height=30, bg="")
    separator.pack()

    var = StringVar(value="option1")

    label = Label(first_window, text="Choose your download option:")
    label.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    option1_button = Radiobutton(first_window, text="Youtube Video", variable=var, value="option1")
    option1_button.pack()

    option2_button = Radiobutton(first_window, text="Local Video", variable=var, value="option2")
    option2_button.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    def open_second_window():
        first_window.destroy()
        second_window = Tk()
        second_window.geometry("400x200")

        if(var.get() == "option1"):

            second_window.title("YOUTUBE")
            
            separator = Frame(second_window, height=10, bg="")
            separator.pack()
            
            entry_label = Label(second_window, text="Put your URL:")
            entry_label.pack()

            entry = Entry(second_window)
            entry.pack()

            separator = Frame(second_window, height=10, bg="")
            separator.pack()

            var2 = StringVar(value="option1")

            option1_button2 = Radiobutton(second_window, text="Download Video", variable=var2, value="option1")
            option1_button2.pack()

            option2_button2 = Radiobutton(second_window, text="Download Video and Subtitle", variable=var2, value="option2")
            option2_button2.pack()

            option3_button2 = Radiobutton(second_window, text="Download Audio", variable=var2, value="option3")
            option3_button2.pack()

            
            def submit_function():
                
                dir_output = os.path.join(os.path.join(os.path.expanduser('~')), 'Videos/')
                file = dir_output+os.listdir(dir_output)[0]

                data = entry.get()

                if(var2.get() == "option3"):
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
                    
                    
                    if(var2.get() == "option2"):
                        subprocess.run(['whisper', file, '--model','base', '--output_dir', dir_output, '--output_format', 'srt'],check=True)
                
                second_window.destroy()

            separator = Frame(second_window, height=10, bg="")
            separator.pack()

            submit_button = Button(second_window, text="Submit", command=submit_function)
            submit_button.pack()

            second_window.mainloop()
        
        else:
            
            second_window.title("LOCAL")
            separator = Frame(second_window, height=20, bg="")
            separator.pack()

            entry_label = Label(second_window, text="Choose your File:")
            entry_label.pack()

            separator = Frame(second_window, height=10, bg="")
            separator.pack()

            def select_file():
                global input_file
                input_file = filedialog.askopenfilename()
                print(input_file)
            
            file_button = Button(second_window, text="Select File", command=select_file)
            file_button.pack()

            separator = Frame(second_window, height=10, bg="")
            separator.pack()

            var3 = StringVar(value="option1")

            option1_button3 = Radiobutton(second_window, text="Transcribe Video", variable=var3, value="option1")
            option1_button3.pack()

            option2_button3 = Radiobutton(second_window, text="Convert to Audio", variable=var3, value="option2")
            option2_button3.pack()

            def submit_action():
                print(input_file)
            
            separator = Frame(second_window, height=10, bg="")
            separator.pack()

            submit_button = Button(second_window, text="Submit", command=submit_action)
            submit_button.pack()

    submit_button = Button(first_window, text="Submit", command=open_second_window)
    submit_button.pack()

    first_window.mainloop()

create_first_window()