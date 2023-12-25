import tkinter as tk
import os
from PIL import ImageTk, Image
from platform import system
from sys import platform, version_info
from tkinter import PhotoImage, Button
import os
import time

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
        
        #make buttons smaller
        BImageB = Image.open("Images/buttons/Blue button.jpeg")
        size = (BImageB.width // 2, BImageB.height // 2)  # Change the size as needed
        m_bib = BImageB.copy()
        m_bib.thumbnail(size)

        sm_bib = ImageTk.PhotoImage(m_bib)
        
        BImageR = Image.open("Images/buttons/LeftButton.jpeg")
        OpeningImage = Image.open("Images/pierwsi.png")

        Guest1 = Image.open('Images/Guests/Aunt_Vasilisa.jpeg')
        Guest2 = Image.open('Images/Guests/Dad_sis_Masha.jpeg')
        Guest3 = Image.open('Images/Guests/Luba_Ludmila.jpeg')
        Guest4 = Image.open('Images/Guests/BF_Boris.jpeg')
        Guest5 = Image.open('Images/Guests/BF_\Katya.jpeg')
        Guest6 = Image.open('Images/Guests/Cousin_Olga.jpeg')
        Guest7 = Image.open('Images/Guests/Dad_Yaroslav.jpeg')
        Guest8 = Image.open('Images/Guests/Grandma_Marzanna.jpeg')
        Guest9 = Image.open('Images/Guests/Grandpa_Gnevomir.jpeg')
        Guest10 = Image.open('Images/Guests/Mom_Borzena.jpeg')
        Guest11 = Image.open('Images/Guests/Sis_Zlata.jpeg')
        Guest12 = Image.open('Images/Guests/Uncle_Mieszko.jpeg')
        ### add-ons
        Addon1 = Image.open('Images/addons/Auntie_tea.jpeg')
        Addon2 = Image.open('Images/addons/Beer.jpeg')
        Addon3 = Image.open('Images/addons/Honey.jpeg')
        Addon4 = Image.open('Images/addons/Juices.jpeg')
        Addon5 = Image.open('Images/addons/Lemon.jpeg')
        Addon6 = Image.open('Images/addons/Salt.jpeg')
        Addon7 = Image.open('Images/addons/Sugar.jpeg')
        Addon8 = Image.open('Images/addons/Tea.jpeg')
        Addon9 = Image.open('Images/addons/Vodka.jpeg')
        Addon10 = Image.open('Images/addons/Wine.jpeg')
        #Tables
        Table1 = Image.open('Images/Table/FishyTable.jpeg')
        Table2 = Image.open('Images/Table/MeatyTable.jpeg')
        Table3 = Image.open('Images/Table/VeganTable.jpeg')
        Table4 = Image.open('Images/Table/VegeTable.jpeg')
        
        

        
        #Lists of images
        Guests_list= [Guest1,Guest2,Guest3,Guest4,Guest5,Guest6,Guest7,Guest8,Guest9,Guest10,Guest11,Guest12]
        addons_list = [Addon1,Addon2,Addon3,Addon4,Addon5,Addon6,Addon7,Addon8,Addon9,Addon10]
        Tables_list = [Table1,Table2,Table3,Table4]
       #ImageTk
        for i in range(len(Guests_list)):
            Guests_list[i] = ImageTk.PhotoImage(Guests_list[i])

        for i in range(len(addons_list)):
            addons_list[i] = ImageTk.PhotoImage(addons_list[i])

        for i in range(len(Tables_list)):
            Tables_list[i] = ImageTk.PhotoImage(Tables_list[i])
        


        BImageB = ImageTk.PhotoImage(BImageB)
        BImageR = ImageTk.PhotoImage(BImageR)
        OpeningImage = ImageTk.PhotoImage(OpeningImage)
        
        Imagesz = tk.Label(image=OpeningImage)     
        Imagesz.image = OpeningImage
        Imagesz.pack( padx="10", pady="10")
        
        #read from Folder descriptions  string and write it to variable make them in ordervasilia masha ludmila boris katya olga yaroslav marzanna gnevomir borzena zlata mieszko
        # Wait for a second after each assignment

        file_path = "True Descriptions.txt"  # Replace with the actual path to your text file

        with open(file_path, 'r') as file:
            content = file.read()

# Split the content into individual descriptions
        descriptions = content.split('- ')

# Remove empty strings and leading/trailing whitespace
        descriptions = [desc.strip() for desc in descriptions if desc.strip()]

            
            

        vasilisa = descriptions[0]
        masha = descriptions[1]
        ludmila = descriptions[2]
        boris = descriptions[3]
        katya = descriptions[4]
        olga = descriptions[5]
        yaroslav = descriptions[6]
        marzanna = descriptions[7]
        gnevomir = descriptions[8]
        borzena = descriptions[9]
        zlata = descriptions[10]
        mieszko = descriptions[11]

        print("Vasilisa: ",vasilisa)
        print()
        print("Masha: ",masha)
        print()
        print("Boris: ",boris)
        print()
        print("Olga: ",olga)
        print()
        print("Marzanna: ",marzanna)
        print()
        print("Borzena: ",borzena)
        print()
        print("Ludmila: ",ludmila)
        print()
        print("Katya: ",katya)
        print()
        print("Yaroslav: ",yaroslav)
        print()
        print("Gnevomir: ",gnevomir)
        print()
        print("Zlata: ",zlata)
        print()
        print("Mieszko: ",mieszko)


        

        # Create buttons
        def Backvard():
            label2.config(text="- Vasilisa: She is your mother's sister, and she is very kind and caring. \nShe loves to cook and bake, and she always makes delicious meals for the family. \nShe is also very creative and loves to make crafts and descriptions for special occasions.")
            
            Imagesz.config(image=Guest1)
            Imagesz.image = Guest1
            Imagesz.pack( padx="10", pady="10")
            

        def Forvard(nmbr):
            
            
            label2.config(text="- Masha: She is your father's sister, and she is very adventurous and outgoing. \nShe loves to travel and explore new places, and she always has exciting stories to share. \nShe is also very athletic and enjoys playing sports and outdoor activities.")            
            Imagesz.config(image=Guests_list[nmbr-1])
            Imagesz.image = Guest2
            Imagesz.pack(padx="10", pady="10")

        ButtonV = Button(self.root, text="<<",command=Backvard, font=("Helvetica", 20, 'bold'), bg="red").pack(side="left", padx="50", pady="50")
        ButtonM = Button(self.root, text=">>", command=lambda: Forvard(2), font=("Helvetica", 20, 'bold'), bg="blue").pack(side="right", padx="50", pady="50")
        #make checkboxes

        # Exit button
        ButtonExit = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green").pack(side="bottom",padx="10", pady="50")
        ButtonNext = Button(self.root, text="Next", font=("Helvetica", 20, 'bold'), command=self.nextParagraph, bg="yellow").pack( side="bottom",padx="10", pady="50")
        ButtonSelect = Button(self.root, text="Select", font=("Helvetica", 20, 'bold'), bg="green").pack(side="bottom",padx="10", pady="10")
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
