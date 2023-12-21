import tkinter as tk
from tkinter import ttk,TkVersion
import customtkinter as ctk
from tkinter import Button
from PIL import ImageTk, Image
import os
from sys import platform, version_info, exit
from platform import system
from sys import version_info
from tkinter import Tk, PhotoImage

class FeastApp: 
    def __init__(self):
        # Create fundamental elements of the application
        self.root = tk.Tk()
        self.root.title("Feast")
        print("Tkinter version:", TkVersion)
        icondir = os.path.join(os.path.dirname(__file__))
        if system() == 'Windows':
            iconfile = os.path.join(icondir, 'Icona.ico')
            self.root.wm_iconbitmap(default=iconfile)
        else:
            icon = PhotoImage(master=self.root, file='Icona.png')
            self.root.wm_iconphoto(True, icon)
        self.root.update_idletasks()
        self.root.geometry("960x900")
        self.root.resizable(False, False)
        self.root.update()

        # Create a Labels widget
        # 1st label
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph!", font=("Lobster", 32))
        label1.pack()
        # 2nd label
        label2 = tk.Label(self.root, text="- Grandfather Ivan: He is your mother's father, and he is very old and wise.\n He likes to tell stories and legends, and he knows a lot about Slavic culture and traditions. \nHe is also very strict and conservative, \nand often scolds guests who do not follow the rules or respect the customs.", font=("Lobster", 16))
        label2.pack()

        # images
        # 1st image
        image1 = Image.open("pierwsi.png")
        image1 = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=image1)
        label1.image = image1
        label1.pack( padx="10", pady="10")


        # Create buttons
        # 1st button
        ButtonV = Button(self.root, text="Vasilisa", font=("Lobster", 20, 'bold'), bg="red")
        ButtonV.pack(side="left", padx="10", pady="10")

        # 2nd button
        ButtonM = Button(self.root, text="Masha", font=("Lobster", 20, 'bold'), bg="blue")
        ButtonM.pack(side="right", padx="10", pady="10")

        # Exit button
        ButtonExit = Button(self.root, text="Exit", font=("Lobster", 20, 'bold'), command=self.root.quit, bg="green")
        ButtonExit.pack(side="bottom", padx="10", pady="50")

        
        

        def __del__(self):
            # Destroy the application
            self.root.destroy()
        
    # Create definitions of methods
    def nextParagraph(self):
            # Create a new paragraph
            pass
    def center_window(self, root):
            width = 960
            height = 860
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    def run(self):
            # Run the application
            self.root.mainloop()       
    

if __name__ == "__main__":
    app = FeastApp()
    app.center_window(app.root)
    app.run()
