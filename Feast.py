import tkinter as tk
import os
from PIL import ImageTk, Image
from platform import system
from sys import platform, version_info
from tkinter import PhotoImage, Button
import os

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
        image1 = Image.open("Images/pierwsi.png")
        image2 = Image.open("Images/Guests/Aunt_Vasilisa.jpeg")
        image3 = Image.open('Images/Guests/Dad_sis_Masha.jpeg')
        Image_list= [image1,image2,image3]
        BImageR = ImageTk.PhotoImage(BImageR)
        image1 = ImageTk.PhotoImage(image1)
        image2 = ImageTk.PhotoImage(image2)
        image3 = ImageTk.PhotoImage(image3)


        Imagesz = tk.Label(image=image1)     
        Imagesz.image = image1
        Imagesz.pack( padx="10", pady="10")
        
        #read from txt file and make it a variable for each family member and give variables name of the guest

        # Read the content from the text file
        

        # Split the content into individual descriptions
        descriptions = []

        # Create variables for each family member
        vasilisa = descriptions[0]
        masha = descriptions[1]
        ivan = descriptions[2]
        igor = descriptions[3]
        natasha = descriptions[4]
        katya = descriptions[5]
        alex = descriptions[6]
        sasha = descriptions[7]
        olga = descriptions[8]
        dasha = descriptions[9]

        # Specify the folder path
        folder_path = 'Skrypty/Descriptionss'

        # Create variables for each family member
        vasilisa = ''
        masha = ''
        mieszko = ''
        borzena = ''
        marzanna = ''
        katya = ''
        ludmila = ''
        yaroslav = ''
        boris = ''
        gnevomir = ''


        # Iterate over the files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()
                    if filename == 'Vasilia description.txt':
                        vasilisa = content
                    elif filename == 'Masha description.txt':
                        masha = content
                    elif filename == 'Mieszko description.txt':
                        mieszko = content
                    elif filename == 'Borzena description.txt':
                        borzena = content
                    elif filename == 'Marzanna description.txt':
                        marzanna = content
                    elif filename == 'Katya description.txt':
                        katya = content
                    elif filename == 'Ludmila description.txt':
                        ludmila = content
                    elif filename == 'Yaroslav description.txt':
                        yaroslav = content
                    elif filename == 'Boris description.txt':
                        boris = content
                    elif filename == 'Gnevomir description.txt':
                        gnevomir = content


        # Create a list of the family members

        #Descri[tion of the family members
        list_of_descriptions = ["- Vasilisa: She is your mother's sister, and she is very kind and caring. \nShe loves to cook and bake, and she always makes delicious meals for the family. \nShe is also very creative and loves to make crafts and decorations for special occasions.",
                                "- Masha: She is your father's sister, and she is very adventurous and outgoing. \nShe loves to travel and explore new places, and she always has exciting stories to share. \nShe is also very athletic and enjoys playing sports and outdoor activities.",
                                "- Ivan: He is your mother's brother, and he is very smart and hardworking. \nHe loves to read and learn new things, and he is always helping others with their problems. \nHe is also very organized and enjoys planning events and activities for the family.",
                                "- Igor: He is your father's brother, and he is very funny and entertaining. \nHe loves to tell jokes and make people laugh, and he always has a positive attitude. \nHe is also very good at sports and enjoys playing games with the family.",
                                "- Natasha: She is your mother's cousin, and she is very artistic and creative. \nShe loves to draw and paint, and she always has a new project she is working on. \nShe is also very friendly and enjoys meeting new people and making friends.",
                                "- Katya: She is your father's cousin, and she is very outgoing and social. \nShe loves to talk and meet new people, and she always has interesting stories to share. \nShe is also very athletic and enjoys playing sports and outdoor activities.",
                                "- Alex: He is your mother's cousin, and he is very smart and hardworking. \nHe loves to read and learn new things, and he is always helping others with their problems. \nHe is also very organized and enjoys planning events and activities for the family.",
                                "- Sasha: He is your father's cousin, and he is very funny and entertaining. \nHe loves to tell jokes and make people laugh, and he always has a positive attitude. \nHe is also very good at sports and enjoys playing games with the family.",
                                "- Olga: She is your mother's cousin, and she is very artistic and creative. \nShe loves to draw and paint, and she always has a new project she is working on. \nShe is also very friendly and enjoys meeting new people and making friends.",
                                "- Dasha: She is your father's cousin, and she is very outgoing and social. \nShe loves to talk and meet new people, and she always has interesting stories to share. \nShe is also very athletic and]
        
        # Create buttons
        def Backvard():
            Imagesz.config(image=image1)
            label2.config(text="- Vasilisa: She is your mother's sister, and she is very kind and caring. \nShe loves to cook and bake, and she always makes delicious meals for the family. \nShe is also very creative and loves to make crafts and decorations for special occasions.")
            
            Imagesz.config(image=image2)
            Imagesz.image = image2
            Imagesz.pack( padx="10", pady="10")
            

        def Forvard():
            label2.config(text="- Masha: She is your father's sister, and she is very adventurous and outgoing. \nShe loves to travel and explore new places, and she always has exciting stories to share. \nShe is also very athletic and enjoys playing sports and outdoor activities.")            
            Imagesz.config(image=image3)
            Imagesz.image = image3
            Imagesz.pack( padx="10", pady="10")

        ButtonV = Button(self.root, text="<<",command=Backvard, font=("Helvetica", 20, 'bold'), bg="red").pack(side="left", padx="10", pady="10")
        ButtonM = Button(self.root, text=">>", command= Forvard, font=("Helvetica", 20, 'bold'), bg="blue").pack(side="right", padx="10", pady="10")
        # Exit button
        ButtonExit = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green").pack(side="bottom",padx="10", pady="50")
        ButtonNext = Button(self.root, text="Next", font=("Helvetica", 20, 'bold'), command=self.nextParagraph, bg="yellow").pack( side="bottom",padx="10", pady="50")
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
