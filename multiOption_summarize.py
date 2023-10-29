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

        if(var.get() == "option1"):
            path = os.path.join(os.getcwd(),"Youtube.py")
            subprocess.run(['python3',path],check=True)
        
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