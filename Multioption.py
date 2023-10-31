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

    def open_option_selected():
        first_window.destroy()

        if(var.get() == "option1"):
            path = os.path.join(os.getcwd(), "Youtube.py")
            subprocess.run(["python3", path], shell=True)
        
        else:
            path = os.path.join(os.getcwd(), "Local.py")
            subprocess.run(["python3", path], shell=True)

    submit_button = Button(first_window, text="Submit", command=open_option_selected)
    submit_button.pack()

    first_window.mainloop()

create_first_window()