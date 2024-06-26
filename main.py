import tkinter as tk
from tkinter import messagebox

# Function to be called when the button is clicked
def on_button_click():
    messagebox.showinfo("Information", "Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Basic GUI")

# Set the window size
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Welcome to the Basic GUI")
label.pack(pady=10)


# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
