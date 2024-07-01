import tkinter as tk


class IntroPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome to the Intro Page", bg="#66b3ff")
        label.pack(pady=10)

        courseLabel = tk.Label(self, text = "Select your course:")
        courseLabel.pack(pady=10)

        self.courseVar = tk.StringVar()
        self.courseVar.set("Select a course")

        courses = ["PCM", "PCMB", "PCB", "CA"]
        courseMenu = tk.OptionMenu(self, self.courseVar, *courses)
        courseMenu.pack(pady=10)

        submit = tk.Button(self, text = "Submit", command= self.submitCourse)
        submit.pack(pady = 10 )

        button = tk.Button(self, text="Back to Main Page", command=lambda: controller.show_frame("MainPage"))
        button.pack(pady=10)

        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)

        self.drawGradient(self.canvas, "#b3d9ff", "#66b3ff")


    def submitCourse(self):
        selectedCourse = self.courseVar.get() #gets a selected course
        print(selectedCourse)
        if selectedCourse == "PCM":
            self.controller.show_frame("PcmPage")
        elif selectedCourse == "PCMB":
            self.controller.show_frame("PcmPage")##
        elif selectedCourse == "PCB":
            self.controller.show_frame("PcmPage")##
        elif selectedCourse == "CA":
            self.controller.show_frame("PcmPage") ##
        else:
            print("Choose one")
            


    def drawGradient(self, canvas, color1, color2):
        for i in range(500):
            r, g, b = self.interpolate_color(color1, color2, i / 500)
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_line(0, i, 500, i, fill=color)

    def interpolate_color(self, color1, color2, factor):
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        r = int(r1 + (r2 - r1) * factor)
        g = int(g1 + (g2 - g1) * factor)
        b = int(b1 + (b2 - b1) * factor)
        return r, g, b
        
