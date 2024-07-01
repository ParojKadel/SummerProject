import tkinter as tk
from intro1 import IntroPage  # Importing the IntroPage class from the intro1 module
from pcm import PcmPage

class App(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.title("Basic GUI")
        self.geometry("500x500")
        self.configure(bg="lightblue")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)  
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  

        for F in (MainPage, IntroPage, PcmPage):
            page_name = F.__name__  
            frame = F(parent=container, controller=self) 
            self.frames[page_name] = frame 
            frame.grid(row=0, column=0, sticky="nsew")  

        self.show_frame("MainPage")  

    def show_frame(self, page_name): 
        frame = self.frames.get(page_name)
        if frame: 
            frame.tkraise() 
        else:
            print(f"No such frame: {page_name}")




class MainPage(tk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)  
        self.controller = controller

        label = tk.Label(self, text="Let's choose your career")
        label.pack(pady=10)

        button = tk.Button(self, text="Go Ahead", command=lambda: controller.show_frame("IntroPage"))
        button.pack(pady=10)
        button.config(bg="red", fg="black")


print(__name__)

if __name__ == "__main__":
    app = App()
    app.mainloop()
