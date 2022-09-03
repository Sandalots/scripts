import tkinter

class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello World"
        self.hi_there.pack(side="top")

        self.quit = tkinter.Button(self, text="QUIT", fg="red")
        self.quit.pack(side="bottom")
    

tkStart = App()
tkStart.mainloop()
        
