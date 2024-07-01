import tkinter as tk

class PcmPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to the PCM Page")
        label.pack(pady=10)

        button = tk.Button(self, text="Return", command=lambda: controller.show_frame("IntroPage"))
        button.pack(pady=10)


