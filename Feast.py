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
               
       

        # Images
        
        #make buttons smaller
        BImageB = Image.open("Images/buttons/Blue button.jpeg")      
        BImageR = Image.open("Images/buttons/LeftButton.jpeg")
        OpeningImage = Image.open("Images/pierwsi.png")

        list_of_paths_Guests = ["Images/Guests/Aunt_Vasilisa.jpeg", "Images/Guests/Dad_sis_Masha.jpeg", "Images/Guests/Luba_Ludmila.jpeg", "Images/Guests/BF_Boris.jpeg", "Images/Guests/BF_Katya.jpeg", "Images/Guests/Cousin_Olga.jpeg", "Images/Guests/Dad_Yaroslav.jpeg", "Images/Guests/Grandma_Marzanna.jpeg", "Images/Guests/Grandpa_Gnevomir.jpeg", "Images/Guests/Mom_Borzena.jpeg", "Images/Guests/Sis_Zlata.jpeg", "Images/Guests/Uncle_Mieszko.jpeg"]
        list_of_paths_Tables = ["Images/Table/FishyTable.jpeg", "Images/Table/MeatyTable.jpeg", "Images/Table/VeganTable.jpeg", "Images/Table/VegeTable.jpeg"]
        list_of_paths_Addons = ["Images/addons/Auntie_tea.jpeg", "Images/addons/Beer.jpeg", "Images/addons/Honey.jpeg", "Images/addons/Juices.jpeg", "Images/addons/Lemon.jpeg", "Images/addons/Salt.jpeg", "Images/addons/Sugar.jpeg", "Images/addons/Tea.jpeg", "Images/addons/Vodka.jpeg", "Images/addons/Wine.jpeg"]
        
        #read from list Guests 1-12 and write it to variable make them in order
        for i ,path in enumerate(list_of_paths_Guests, start=1):
            var_name = f"Guest{i}" 
            globals()[var_name] = Image.open(path)
        #read from list Tables 1-4 and write it to variable make them in order
        for i ,path in enumerate(list_of_paths_Tables, start=1):
            var_name = f"Table{i}" 
            globals()[var_name] = Image.open(path)
        #read from list addons 1-10 and write it to variable make them in order
        for i ,path in enumerate(list_of_paths_Addons, start=1):
            var_name = f"Addon{i}" 
            globals()[var_name] = Image.open(path)
        
            
        
        

        
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
        
        label2 = tk.Label(self.root, text="Please meet the family members and get to know them." , font=("Helvetica", 16),background="#BAA391")
        label2.pack()
        file_path = "True Descriptions.txt"  # Replace with the actual path to your text file

        with open(file_path, 'r') as file:
            content = file.read()

# Split the content into individual descriptions
        descriptions = content.split('- ')
        #make sure descriptions is at least 12
        while len(descriptions) < 13:
            descriptions.append("")
       


# Remove empty strings and leading/trailing whitespace
        descriptions = [desc.strip() for desc in descriptions if desc.strip()]

        vasilisa = descriptions[0]
        print(vasilisa)
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
     
        
        # Create buttons
        def Backvard():
            label1.config(text='''Please meet the family members 
                and get to know them.''')
            Imagesz.pack( side ="top",padx="10", pady="10")
            label2.config(text=vasilisa)
            Imagesz.config(image=Guests_list[0])
            Imagesz.image = Guest1
            

        def Forvard(nmbr):
            label1.config(text='''Please meet the family members 
                and get to know them.''')
            Imagesz.config(image=Guests_list[nmbr-1])
            Imagesz.image = Guest2
            Imagesz.pack(side ="top",padx="10", pady="10")
            label2.config(text=masha)

        ButtonV = Button(self.root, text="<<",command= Backvard, font=("Helvetica", 20, 'bold'), bg="red").pack(side="left", padx="10", pady="10")
        ButtonM = Button(self.root, text=">>", command=lambda: Forvard(2), font=("Helvetica", 20, 'bold'), bg="blue").pack(side="right", padx="10", pady="10")
        #make checkboxes

        # Exit button
        ButtonNext = Button(self.root, text="Next", font=("Helvetica", 20, 'bold'), command=self.nextParagraph, bg="yellow").pack( side="right",padx="10", pady="10")
        ButtonSelect = Button(self.root, text="Select", font=("Helvetica", 20, 'bold'), bg="green").pack(side="left",padx="10", pady="10")
        ButtonExit = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green").pack(side="bottom",padx="10", pady="10")
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
            if platform == "linux" :
                self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
            else:
                # move the window to the center of the screen for Windows 
                x,y = (screen_width/2) - (width/2), (screen_height/2) - (height//2.5)

                self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')



    
    def run(self):
            # Run the application
            self.root.mainloop()   

if __name__ == "__main__":
    app = FeastApp()
    app.center_window(app.root)
    app.run()
