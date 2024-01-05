import tkinter as tk
import os
from PIL import ImageTk, Image
from platform import system
from sys import platform, version_info
from tkinter import PhotoImage, Button, Text, Scrollbar

class FeastApp: 
    def __init__(self):
# Create fundamental elements of the application
        self.root = tk.Tk()
        self.inizialize_root()

        self.load_images()
        self.Create_variables()
        self.load_descriptions()
        self.center_window(self.root)
        self.Gui_()


        
    def inizialize_root(self):
        self.root.title("Feast")
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


        #Selected variables
        self.selected_guests = set()
        self.selected_tables = None

    def load_images(self):
        guests_paths = ["Images/Guests/Aunt_Vasilisa.png", "Images/Guests/Dad_sis_Masha.png", "Images/Guests/Luba_Ludmila.png", "Images/Guests/BF_Boris.png", "Images/Guests/BF_Katya.png", "Images/Guests/Cousin_Olga.png", "Images/Guests/Dad_Yaroslav.png", "Images/Guests/Grandma_Marzanna.png", "Images/Guests/Grandpa_Gnevomir.png", "Images/Guests/Mom_Borzena.png", "Images/Guests/Sis_Zlata.png", "Images/Guests/Uncle_Mieszko.png"]
        tables_paths = ["Images/Table/FishyTable.png", "Images/Table/MeatyTable.png", "Images/Table/VeganTable.png", "Images/Table/VegeTable.png"]
        addons_paths = ["Images/addons/Auntie_tea.png", "Images/addons/Beer.png", "Images/addons/Honey.png", "Images/addons/Juices.png", "Images/addons/Lemon.png", "Images/addons/Salt.png", "Images/addons/Sugar.png", "Images/addons/Tea.png", "Images/addons/Vodka.png", "Images/addons/Wine.png"]
        # Create a dictionary of images
        self.guests = {f"Guest{i}": Image.open(path) for i, path in enumerate(guests_paths, start=1)}
        self.tables = {f"Table{i}": Image.open(path) for i, path in enumerate(tables_paths, start=1)}
        self.addons = {f"Addon{i}": Image.open(path) for i, path in enumerate(addons_paths, start=1)}
           

            # Convert images to ImageTk format
        self.guest_images = {key: ImageTk.PhotoImage(image) for key, image in self.guests.items()}
        self.table_images = {key: ImageTk.PhotoImage(image) for key, image in self.tables.items()}
        self.addon_images = {key: ImageTk.PhotoImage(image) for key, image in self.addons.items()}  

    def Create_variables(self):
        self.family_members = ["Vasilisa", "Masha", "Ludmila", "Boris", "Katya", "Olga", "Yaroslav", "Marzanna", "Gnevomir", "Borzena", "Zlata", "Mieszko"]
        self.SelectGuest = {member: False for member in self.family_members}

        self.types_of_tables = ["Fishy", "Meaty", "Vegan", "Vege"]
        self.SelectTable = {table: False for table in self.types_of_tables}

        self.types_of_addons = ["Auntie_tea", "Beer", "Honey", "Juices", "Lemon", "Salt", "Sugar", "Tea", "Vodka", "Wine"]
        self.SelectAddon = {addon: False for addon in self.types_of_addons}

    def load_descriptions(self):
        file_path = "True Descriptions.txt"  # char description
        file_path2 = "Tables Description.txt"  # table description
        #file_path3 = "Addons Description.txt" # addons description
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()
        with open(file_path2, 'r') as file:
            content2 = file.read()
        '''with open(file_path3, 'r') as file:
            content3 = file.read()'''

        # Split the content into individual descriptions
        descriptions = content.split('- ')
        descriptions2 = content2.split('- ')
        #descriptions3 = content3.split('- ')
        
        descriptions = [desc.strip() for desc in descriptions if desc.strip()]
        descriptions2 = [desc.strip() for desc in descriptions2 if desc.strip()]
        #descriptions3 = [desc.strip() for desc in descriptions3 if desc.strip()]
        # Assign each description to a variable
        self.guest_descriptions = {
            self.family_members[i]: descriptions[i] for i in range(len(self.family_members))
        }
        self.table_descriptions = {
            self.types_of_tables[i]: descriptions2[i] for i in range(len(self.types_of_tables))
        }
        '''self.addon_descriptions = {
            self.types_of_addons[i]: descriptions3[i] for i in range(len(self.types_of_addons))
        }'''

    def Gui_(self):
        #Labels
        # First label for the title
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32),background="#BAA391")
        label1.pack()        
        # Second label for the description
        label2 = tk.Label(self.root, text="Please meet the family members and get to know them." , font=("Helvetica", 16),background="#BAA391")
        label2.pack()   
        # Create an entry image 
        OpeningImage = Image.open("Images/pierwsi.png")
        OpeningImage = ImageTk.PhotoImage(OpeningImage)
        Imagesz = tk.Label(image=OpeningImage)     
        Imagesz.image = OpeningImage
        Imagesz.pack()  

        #buttons
        # Create buttons for navigation 
        ForvardButton = Button(self.root, text=">>\n>>\n>>", command=lambda: update_display(1), font=("Helvetica", 20, 'bold'), bg="blue")
        BackvardButton = Button(self.root, text="<<\n<<\n<<",command= lambda: update_display(), font=("Helvetica", 20, 'bold'), bg="red")
        # Status bar
        status = tk.Label(self.root, text="Status: Start",font= ("Helvetica",20) , bd=1,bg="#BAA391", relief='sunken', anchor='e')
        status.pack(side="bottom", fill="x")
        # Exit button
        ButtonExit = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green").pack(side="bottom", padx=10, pady=10, anchor="s")
        # Select button
        ButtonSelect = Button(self.root, text="Select", font=("Helvetica", 20, 'bold'), command= lambda: select_item(mode='G') ,  bg="green")
        # Next button
        FoodButton = Button(self.root, text="Select Tables", font=("Helvetica", 20, 'bold'), command=lambda: update_display(1,mode = 'F'), bg="yellow").pack(side="bottom", padx=10, pady=10, anchor="s")
        # Continue button
        GuestsButton = Button(self.root, text="Select Guests", font=("Helvetica", 20, 'bold'), command=lambda:update_display(1), bg="yellow")
        GuestsButton.pack( side="bottom",padx=10, pady=10)
        
        
# Create functions
        def update_display(nmbr, mode='G'):
            var = nmbr - 1
            g_status= len(self.guests.values())
            t_status= len(self.tables.values())
            #a_status= len(self.addons.values())
            
            if mode == 'F':
                label1.config(text="Please choose the type of food.")
                t_descriptions = list(self.table_descriptions.values())
                label2.config(text=t_descriptions[var])
                t_images = list(self.table_images.values())
                
                Imagesz.config(image=t_images[var])
                Imagesz.image = t_images[nmbr]
                status.config(text=f"Status: {nmbr}/{t_status}")
                ButtonSelect.config(command=lambda: select_item(mode='F'))
            

                Imagesz.config(image=t_images[var])
                for _ in t_images:
                    print(_)
                print(t_images[var])
                Imagesz.image = t_images[nmbr]
                status.config(text=f"Status: {nmbr}/{t_status}")
                ButtonSelect.config(command=lambda: select_item(mode='F'))
            elif mode == 'G':
                label1.config(text="Please meet the family members\n and get to know them.")
                g_descriptions = list(self.guest_descriptions.values())
                g_images = list(self.guest_images.values())
                
                label2.config(text=g_descriptions[var])
                Imagesz.config(image=g_images[var])
                Imagesz.image = g_images[nmbr]
                status.config(text=f"Status: {nmbr}/{g_status}")
                ButtonSelect.config(command=lambda: select_item(mode='G'))
                
            '''elif mode == 'A':
                label1.config(text="Please choose the addons.")
                a_descriptions = list(self.addon_descriptions.values())
                a_images = list(self.addon_images.values())
                label2.config(text=a_descriptions[var])
                Imagesz.config(image=a_images[var])
                Imagesz.image = a_images[nmbr]
                status.config(text=f"Status: {nmbr}/{a_status}")
                ButtonSelect.config(command=lambda: select_item(mode='A'))'''
                       
            val = nmbr+1
            label2.pack()
            Imagesz.pack()
            GuestsButton.config(text="")
            GuestsButton.pack_forget()
            ButtonSelect.pack(side="bottom", padx=10, pady=10, anchor="s")
            BackvardButton.config(command=lambda: update_display(var, mode))
            BackvardButton.pack(side="left", padx=10, pady=10, anchor="w")
            ForvardButton.config(command=lambda: update_display(val, mode))
            ForvardButton.pack(side="right", padx=10, pady=10, anchor="e")
            if mode == 'G':
                ForvardButton.config(state="disabled") if var == 12 else ForvardButton.config(state="normal")
                BackvardButton.config(state="disabled") if nmbr == 1 else BackvardButton.config(state="normal")
            elif mode == 'F':
                ForvardButton.config(state="disabled") if nmbr == 4 else ForvardButton.config(state="normal")
                BackvardButton.config(state="disabled") if nmbr == 1 else BackvardButton.config(state="normal")
            '''else:
                ForvardButton.config(state="disabled") if nmbr == a_status else ForvardButton.config(state="normal")
                BackvardButton.config(state="disabled") if nmbr == 1 else BackvardButton.config(state="normal")'''

        def select_item(mode='G'):
            current_index = int(status.cget("text").split(":")[1].split("/")[0]) - 1
            imgpath = "Images/Oki.png"
            img2path = "Images/Nah.png"
            img = Image.open(imgpath)
            img2 = Image.open(img2path)
            img = img.resize((100, 100))
            img2 = img2.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            img2 = ImageTk.PhotoImage(img2)
            label3 = tk.Label(self.root, font=("Helvetica", 16), fg="red", bg="#BAA391")
            label3.pack()
            label4 = tk.Label(self.root, image=img2, background="#BAA391")
            label4.image = img2
            label4.pack()
            label3.after(2000, lambda: label3.destroy())
            label4.after(2000, lambda: label4.destroy())

            if mode == 'F':
                current_table = self.types_of_tables[current_index]
                self.SelectTable[current_table] = not self.SelectTable[current_table]
                label3.config(text=f"{current_table} is not selected")
                if self.SelectTable[current_table] == True:
                    label3.config(text=f"{current_table} is selected", fg="green")
                    label4.config(image=img)
                    label4.image = img
                    self.selected_tables = int(self.types_of_tables[current_table])
                    ButtonSelect.pack_forget()
                    DeselectButton = Button(self.root, text="Deselect", font=("Helvetica", 20, 'bold'), command=lambda: update_display(1, 'F'), bg="red")
                    DeselectButton.pack(side="bottom", padx=10, pady=10, anchor="s")
                    GuestsButton.pack(side="bottom", padx=10, pady=10)
            elif mode == 'G':
                current_member = self.family_members[current_index]
                self.SelectGuest[current_member] = not self.SelectGuest[current_member]
                label3.config(text=f"{current_member} is not selected")
                if self.SelectGuest[current_member] == True:
                    label3.config(text=f"{current_member} is selected", fg="green")
                    label4.config(image=img)
                    label4.image = img

   

        def __del__(self):
            # Destroy the application
            self.root.destroy()
        
# Create definitions of methods
        
    def center_window(self, root):
            width,height = 980, 1000
            screen_width,screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            x,y = (screen_width/2) - (width/2), (screen_height/2) - (height)
            if platform == "linux" :
                self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
            else:
                # move the window to the center of the screen for Windows 
                x,y = (screen_width/2) - (width/2), (screen_height/2) - (height//1.9)
                self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    
    def run(self):
            # Run the application
            self.root.mainloop()   

if __name__ == "__main__":
    app = FeastApp()
    app.center_window(app.root)
    app.run()


