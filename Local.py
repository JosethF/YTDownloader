from tkinter import Tk, Label, Radiobutton, StringVar, Button, Frame, filedialog
import subprocess
import os

# Declare input_file as a global variable with an initial value of None for handle it empty files
input_file = None

# Function to create the main window
def create_first_window():
    # Create a Tkinter window
    first_window = Tk()
    first_window.title("LOCAL")  # Set window title
    first_window.geometry("400x200")  # Set window dimensions

    # Create a separator frame for spacing
    separator = Frame(first_window, height=20, bg="")
    separator.pack()

    # Label to instruct the user to choose a file
    entry_label = Label(first_window, text="Choose your File:")
    entry_label.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    # Function to display an error window if no file is selected
    def error_empty_file_window():
        second_window = Tk()
        second_window.title("Empty File")
        second_window.geometry("250x70")

        separator = Frame(second_window, height=20, bg="")
        separator.pack()

        label = Label(second_window, text="Please Select a File")
        label.pack()

    # Function to handle file selection using file dialog
    def select_file():
        global input_file
        # Ask the user to select a file and store the file path in input_file variable
        input_file = filedialog.askopenfilename()

    # Button to trigger the file selection function
    file_button = Button(first_window, text="Select File", command=select_file)
    file_button.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    # Variable to store the selected radio button option
    var3 = StringVar(value="option1")

    # Radio buttons for selecting the operation (Transcribe Video or Convert to Audio)
    option1_button3 = Radiobutton(first_window, text="Transcribe Video", variable=var3, value="option1")
    option1_button3.pack()

    option2_button3 = Radiobutton(first_window, text="Convert to Audio", variable=var3, value="option2")
    option2_button3.pack()

    # Function to handle the submission of the form
    def submit_action():
        # Path for the new folder where output files will be saved
        new_folder = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', '4to3')
        
        # Check if no file is selected, show an error window
        if input_file is None:
            error_empty_file_window()
        else:
            # If the folder doesn't exist, create it
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            # Check the selected option and perform the corresponding action
            if var3.get() == "option1" :
                # Run the 'whisper' command for video transcription
                subprocess.run(['whisper', input_file, '--model','base', '--output_dir', new_folder, '--output_format', 'srt', '--fp16', 'False'],check=True)
            elif var3.get() == "option2" :
                # Extract the file name without extension and create an output file path with .mp3 extension
                output_file = os.path.join(new_folder, os.path.basename(input_file[0:input_file.find(".")])+".mp3")
                # Run the FFmpeg command for audio conversion
                subprocess.run(["ffmpeg", "-y", "-i", input_file, "-q:a", "0", "-map", "a", output_file], shell=True)

        # Destroy the main window after processing
        first_window.destroy()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    # Trigger submission function
    submit_button = Button(first_window, text="Submit", command=submit_action)
    submit_button.pack()

    # Start the main event loop for the tkinter application
    first_window.mainloop()

# Call the function to create the main window
create_first_window()
