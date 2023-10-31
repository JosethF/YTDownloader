from tkinter import Tk, Label, Radiobutton, StringVar, Button, Frame
import os
import subprocess

# Function to create the main window
def create_first_window():
    # Create a Tkinter window
    first_window = Tk()
    first_window.title("Choose your download option:")
    first_window.geometry("400x200")

    # Create a separator frame for spacing
    separator = Frame(first_window, height=30, bg="")
    separator.pack()

    # Variable to store the selected radio button option
    var = StringVar(value="option1")

    # Label to instruct the user to choose a download option
    label = Label(first_window, text="Choose your download option:")
    label.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    # Radio buttons for selecting download options (Youtube Video or Local Video)
    option1_button = Radiobutton(first_window, text="Youtube Video", variable=var, value="option1")
    option1_button.pack()

    option2_button = Radiobutton(first_window, text="Local Video", variable=var, value="option2")
    option2_button.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    # Function to handle the selection and open the chosen option
    def open_option_selected():
        # Close the main window
        first_window.destroy()

        # Check the selected option and open the corresponding Python script
        if(var.get() == "option1"):
            # Run the Youtube.py script using subprocess
            path = os.path.join(os.getcwd(), "Youtube.py")
            subprocess.run(["python3", path], shell=True)
        else:
            # Run the Local.py script using subprocess
            path = os.path.join(os.getcwd(), "Local.py")
            subprocess.run(["python3", path], shell=True)

    # Button to submit the form and trigger the selection function
    submit_button = Button(first_window, text="Submit", command=open_option_selected)
    submit_button.pack()

    # Start the main event loop for the tkinter application
    first_window.mainloop()

# Call the function to create the main window
create_first_window()
