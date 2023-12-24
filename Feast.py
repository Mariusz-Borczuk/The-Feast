import tkinter as tk
import os
from PIL import ImageTk, Image
from platform import system
from sys import platform, version_info
from tkinter import PhotoImage, Button

class FeastApp: 
    def __init__(self):
        # Create fundamental elements of the application
        self.root = tk.Tk()
        self.root.title("Feast")
        #change background colour to page like
        self.root.configure(background="#BAA391")
        icondir = os.path.join(os.path.dirname(__file__))
        if system() == 'Windows':
            iconfile = os.path.join(icondir, 'Icona.ico')
            self.root.wm_iconbitmap(default=iconfile)
        else:
            icon = PhotoImage(master=self.root, file='Icona.png')
            self.root.wm_iconphoto(True, icon)
        self.root.update_idletasks()
        self.root.resizable(False, False)
        self.root.update()

        # Create a Labels widget
        # 1st label
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32),background="#BAA391")
        label1.pack(side = "top")
        # 2nd label
               
        label2 = tk.Label(self.root, text="Please meet the family members and get to know them." , font=("Helvetica", 16),background="#BAA391")
        label2.pack()

        # Images
        
        
        BImageB = Image.open("Images/buttons/Blue button.jpeg")
        BImageB = ImageTk.PhotoImage(BImageB)
        BImageR = Image.open("Images/buttons/LeftButton.jpeg")
        BImageR = ImageTk.PhotoImage(BImageR)
        image1 = Image.open("Images/pierwsi.png")
        image1 = ImageTk.PhotoImage(image1)
        image2 = Image.open("Images/Aunt_Vasilisa.jpeg")
        image2 = ImageTk.PhotoImage(image2)
        image3 = Image.open('Images/Dad_sis_Masha.jpeg')
        image3 = ImageTk.PhotoImage(image3)


        Imagesz = tk.Label(image=image1)     
        Imagesz.image = image1
        Imagesz.pack( padx="10", pady="10")
        
        
        # Create buttons
        def Klick_V():
            Imagesz.config(image=image1)
            label2.config(text="- Vasilisa: She is your mother's sister, and she is very kind and caring. \nShe loves to cook and bake, and she always makes delicious meals for the family. \nShe is also very creative and loves to make crafts and decorations for special occasions.")
            
            Imagesz.config(image=image2)
            Imagesz.image = image2
            Imagesz.pack( padx="10", pady="10")
            

        def Klick_M():
            ZmnButton2 = "Masha"
            label2.config(text="- Masha: She is your father's sister, and she is very adventurous and outgoing. \nShe loves to travel and explore new places, and she always has exciting stories to share. \nShe is also very athletic and enjoys playing sports and outdoor activities.")
            
            Imagesz.config(image=image3)
            Imagesz.image = image3
            Imagesz.pack( padx="10", pady="10")

        ButtonV = Button(self.root, text="Vasilisa",command=Klick_V, font=("Helvetica", 20, 'bold'), bg="red").pack(side="left", padx="10", pady="10")
        ButtonM = Button(self.root, image=  BImageB, text="Masha", command= Klick_M,font=("Helvetica", 20, 'bold'), bg="blue").pack(side="right", padx="10", pady="10")
        # Exit button
        ButtonExit = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green").pack(padx="10", pady="50")
        ButtonNext = Button(self.root, text="Next", font=("Helvetica", 20, 'bold'), command=self.nextParagraph, bg="yellow").pack(side="bottom", padx="10", pady="50")
        def __del__(self):
            # Destroy the application
            self.root.destroy()
        
    # Create definitions of methods
    def nextParagraph(self):
            # Create a new paragraph
            pass
        
    def center_window(self, root):
            width,height = 980, 1080
            screen_width,screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
            x,y = (screen_width/2) - (width/2), (screen_height/2) - (height)
            self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    
    def run(self):
            # Run the application
            self.root.mainloop()   

if __name__ == "__main__":
    app = FeastApp()
    app.center_window(app.root)
    app.run()
