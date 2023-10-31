from tkinter import Tk, Label, Radiobutton, StringVar, Entry, Button, Frame
import os
import subprocess
import yt_dlp

data = None

# Function to create the main window
def create_first_window():
    # Create a Tkinter window
    first_window = Tk()
    first_window.title("Choose your download option:")
    first_window.geometry("400x220")

    # Create a separator frame for spacing
    separator = Frame(first_window, height=20, bg="")
    separator.pack()

    # Label to instruct the user to enter the URL
    label = Label(first_window, text="Put your URL:")
    label.pack()

    separator = Frame(first_window, height=5, bg="")
    separator.pack()

    # Entry widget for user to input the URL
    entry = Entry(first_window)
    entry.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    # Variable to store the selected radio button option
    var = StringVar(value="option1")

    # Radio buttons for selecting the download options
    option1 = Radiobutton(first_window, text="Download Video", variable=var, value="option1")
    option1.pack()

    option2 = Radiobutton(first_window, text="Download Video and Subtitle", variable=var, value="option2")
    option2.pack()

    option3 = Radiobutton(first_window, text="Download Audio", variable=var, value="option3")
    option3.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    # Function to handle the submission of the form
    def submit_function():
        # Output directory for downloaded files
        dir_output = os.path.join(os.path.join(os.path.expanduser('~')), "Desktop/",'YTDownloader/')
        
        # Get the URL entered by the user
        data = entry.get()

        # Download options based on user choice
        if(var.get() == "option3"):
            # Output directory for audio files
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

            # Create the yt_dlp downloader object and start the audio download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([data])

        else:                    
            # Video download options
            ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': dir_output+'%(title)s.%(ext)s',
            }

            # Create the yt_dlp downloader object and start the video download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([data])
            
            # If user chose to download video and subtitles, use 'whisper' to extract subtitles
            if(var.get() == "option2"):
                file = dir_output+os.listdir(dir_output)[0]
                subprocess.run(['whisper', file, '--model','base', '--output_dir', dir_output, '--output_format', 'srt', '--language', 'English', '--fp16', 'False'],check=True)
        
        # Close the main window after processing
        first_window.destroy()

    # Trigger the submission function
    submit_button = Button(first_window, text="Submit", command=submit_function)
    submit_button.pack()

    # Start the main event loop for the tkinter application
    first_window.mainloop()

# Call the function to create the main window
create_first_window()
