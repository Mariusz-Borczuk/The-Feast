import os
from pygame import mixer
import tkinter as tk
from platform import system
from PIL import ImageTk, Image
from sys import platform, version_info
from tkinter import PhotoImage, Button, Text

class FeastApp: 
    def __init__(self):
# Create fundamental elements of the application
        self.root = tk.Tk()
        self.inizialize_root()

        self.load_images()
        self.Create_variables()
        self.load_descriptions()
        self.center_window(self.root)
        #self.selecting_guests()
        #self.selecting_tables()
        #self.selecting_addons()
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



    def load_images(self):
        guests_paths = ["Images/Guests/Aunt_Vasilisa.png", "Images/Guests/Dad_sis_Masha.png", "Images/Guests/Luba_Ludmila.png", "Images/Guests/BF_Boris.png", "Images/Guests/BF_Katya.png", "Images/Guests/Cousin_Olga.png", "Images/Guests/Dad_Yaroslav.png", "Images/Guests/Grandma_Marzanna.png", "Images/Guests/Grandpa_Gnevomir.png", "Images/Guests/Mom_Borzena.png", "Images/Guests/Sis_Zlata.png", "Images/Guests/Uncle_Mieszko.png"]
        tables_paths = ["Images/Table/FishyTable.png", "Images/Table/MeatyTable.png", "Images/Table/VeganTable.png", "Images/Table/VegeTable.png"]
        addons_paths = ["Images/Addons/Auntie_tea.png", "Images/Addons/Beer.png", "Images/Addons/Honey.png", "Images/Addons/Juices.png", "Images/Addons/Lemon.png", "Images/Addons/Salt.png", "Images/Addons/Sugar.png", "Images/Addons/Tea.png", "Images/Addons/Vodka.png", "Images/Addons/Wine.png"]
        # Create a dictionary of images
        self.guests = {f"Guest{i}": Image.open(path) for i, path in enumerate(guests_paths, start=1)}
        self.tables = {f"Table{i}": Image.open(path) for i, path in enumerate(tables_paths, start=1)}
        self.addons = {f"Addon{i}": Image.open(path) for i, path in enumerate(addons_paths, start=1)}
           

            # Convert images to ImageTk format
        self.guest_images = {key: ImageTk.PhotoImage(image) for key, image in self.guests.items()}
        self.table_images = {key: ImageTk.PhotoImage(image) for key, image in self.tables.items()}
        self.addon_images = {key: ImageTk.PhotoImage(image) for key, image in self.addons.items()}  

    def Create_variables(self):
        self.family_members = {"Aunt Vasilia": False, "Masha": False, "Luba Ludmila": False, "Boris": False, "Katya": False, "Olga": False, "Yaroslav": False, "Marzanna": False, "Gnevomir": False, "Borzena": False, "Zlata": False, "Mieszko": False}
        print(len(self.family_members))
        self.types_of_tables = {"Fishy Table": False, "Meaty Table": False, "Vegan Table": False, "Vege Table": False}

        self.types_of_addons = {"Aunties_Tea": False, "Beer": False, "Honey": False, "Juices": False, "Lemon": False, "Salt": False, "Sugar": False, "Tea": False, "Vodka": False, "Wine": False}
    
    def load_descriptions(self):
        file_path = "True Descriptions.txt"  # char description
        file_path2 = "Tables Description.txt"  # table description
        file_path3 = "Addons Description.txt" # addon description
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()
        with open(file_path2, 'r') as file:
            content2 = file.read()
        with open(file_path3, 'r') as file:
            content3 = file.read()

        # Split the content into individual descriptions
        descriptions = content.split('* ')
        descriptions2 = content2.split('* ')
        descriptions3 = content3.split('* ')
        
        descriptions = [desc.strip() for desc in descriptions if desc.strip()]
        descriptions2 = [desc.strip() for desc in descriptions2 if desc.strip()]
        descriptions3 = [desc.strip() for desc in descriptions3 if desc.strip()]
        
        # Assign each description to a variable
        self.guest_descriptions = {
            list(self.family_members.keys())[i]: descriptions[i] for i in range(len(self.family_members))
            }
        self.table_descriptions = {
            list(self.types_of_tables.keys())[i]: descriptions2[i] for i in range(len(self.types_of_tables))
            }
        self.addon_descriptions = {
            list(self.types_of_addons.keys())[i]: descriptions3[i] for i in range(len(self.types_of_addons))
            }

    def Gui_(self):

        #Labels
        # First label for the title
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32),background="#BAA391")
        label1.pack()        
        # Create an entry image 
        OpeningImage = Image.open("Images/pierwsi.png")
        OpeningImage = ImageTk.PhotoImage(OpeningImage)
        Imagesz = tk.Label(image=OpeningImage)     
        Imagesz.image = OpeningImage
        Imagesz.pack()  
        # Second label for the description
        label2 = tk.Label(self.root, text="Please meet the family members and get to know them." , font=("Helvetica", 14),background="#BAA391")
        label2.pack()   
        
        #buttons
        # Create buttons for navigation 
        nmbr = 1  # Define the variable "nmbr"
        mode = 'G'  # Define the variable "mode"
        ForvardButton = Button(self.root, text=">>\n>>\n>>", command=lambda: update_display(1), font=("Helvetica", 20, 'bold'), bg="blue")
        BackvardButton = Button(self.root, text="<<\n<<\n<<",command= lambda: update_display(), font=("Helvetica", 20, 'bold'), bg="red")
        #Audio button
        PlayaudioButton = Button(self.root, text="Play audio", font=("Helvetica", 20, 'bold'), command=lambda: play_audio(nmbr, mode), bg="yellow")

        # Status bar
        status = tk.Label(self.root, text="Status: Start",font= ("Helvetica",20) , bd=1,bg="#BAA391", relief='sunken', anchor='e')
        status.pack(side="bottom", fill="x")
        # Exit button
        ButtonExit = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green").pack(side="bottom", padx=10, pady=5, anchor="s")
        # Select button
        ButtonSelect = Button(self.root, text="Select", font=("Helvetica", 20, 'bold'), command= lambda: select_item(mode='G') ,  bg="green")
        ButtonSelect.place(relx=0.1, rely=0.9, anchor='s')     
        # Deselect button
        ButtonDeselect = Button(self.root, text="Deselect", font=("Helvetica", 20, 'bold'), command=lambda: deselect_button(mode='F'), bg="red")
        ButtonDeselect.place(relx=0.1, rely=0.95, anchor='s')

        # Food button
        FoodButton = Button(self.root, text="Select Tables", font=("Helvetica", 20, 'bold'), command=lambda: update_display(1,mode = 'F'), bg="yellow")
        FoodButton.pack( side="bottom",padx=10, pady=5)
        # Guests button
        GuestsButton = Button(self.root, text="Select Guests", font=("Helvetica", 20, 'bold'), command=lambda:update_display(1), bg="yellow")
        GuestsButton.pack( side="bottom",padx=10, pady=5)
        # Addons button
        AddonsButton = Button(self.root, text="Select Addons", font=("Helvetica", 20, 'bold'), command=lambda:update_display(1, mode='A'), bg="yellow")
        AddonsButton.pack( side="bottom",padx=10, pady=5)
        
# Create functions
        def determine_audio_path(nmbr, mode):
            list_of_audio_paths_guests = ["V.wav","Mas.wav","Lu.wav","Br.wav","Ka.wav","Ol.wav","Ya.wav","Ma.wav","Gn.wav","Bo.wav","Zl.wav","Mi.wav"]
            list_of_audio_paths_tables = ["Fish.mp3", "Meat.mp3", "Vegan.mp3", "Vege.mp3"]
            list_of_audio_paths_addons = ["Vastea.mp3", "Beer.mp3", "Honey.mp3", "Juices.mp3", "Lemon.mp3", "Salt.mp3", "Sugar.mp3", "Tea.mp3", "Vodka.mp3", "Vine.mp3"]
            if mode == 'G':
                return list_of_audio_paths_guests[nmbr-1]
            elif mode == 'F':
                return list_of_audio_paths_tables[nmbr-1]
            else:
                return list_of_audio_paths_addons[nmbr-1]
        
        def play_audio(nmbr, mode):
            audio_path = determine_audio_path(nmbr, mode)
            print(audio_path)
            mixer.init()
            mixer.music.load(audio_path)
            mixer.music.play()
            
        def update_display(nmbr, mode='G'):
            var = nmbr - 1
            g_status = len(self.guests.values())
            t_status = len(self.tables.values())
            a_status = len(self.addons.values())

            if mode == 'F':
                label1.config(text="Please choose the type of food.")
                t_descriptions = list(self.table_descriptions.values())
                label2.config(text=t_descriptions[var])
                t_images = list(self.table_images.values())
                status.config(text=f"Status: {nmbr}/{t_status}")
                current_index = int(status.cget("text").split(":")[1].split("/")[0])

                ButtonSelect.config(command=lambda: select_item(mode='F'))
                ButtonSelect.place(relx=0.1, rely=0.9, anchor='s')
                ButtonDeselect.config(command=lambda: deselect_button(mode='F'))
                ButtonDeselect.place(relx=0.1, rely=0.95, anchor='s')
                
                Imagesz.config(image=t_images[current_index-1])
                Imagesz.image = t_images[current_index-1]

                PlayaudioButton.config(command=lambda: play_audio(nmbr, mode='F'))
                PlayaudioButton.place(relx=0.99, rely=0.95, anchor='e')
            elif mode == 'G':
                label1.config(text="Please meet the family members\n and get to know them.")
                g_descriptions = list(self.guest_descriptions.values())
                g_images = list(self.guest_images.values())
                status.config(text=f"Status: {nmbr}/{g_status}")
                current_index = int(status.cget("text").split(":")[1].split("/")[0])
                label2.config(text=g_descriptions[var])
                Imagesz.config(image=g_images[current_index-1])
                Imagesz.image = g_images[current_index-1]
                PlayaudioButton.config(command=lambda: play_audio(nmbr, mode='G'))
                PlayaudioButton.place(relx=0.99, rely=0.95, anchor='e')
                ButtonSelect.config(command=lambda: select_item(mode='G')).place(relx=0.1, rely=0.9, anchor='s')
                ButtonDeselect.config(command=lambda: deselect_button(mode='G')).place(relx=0.1, rely=0.95, anchor='s')
            elif mode == 'A':
                label1.config(text="Please choose the addons up to 6.")
                a_descriptions = list(self.addon_descriptions.values())
                a_images = list(self.addon_images.values())
                status.config(text=f"Status: {nmbr}/{a_status}")
                current_index = int(status.cget("text").split(":")[1].split("/")[0])
                label2.config(text=a_descriptions[var])
                Imagesz.config(image=a_images[current_index-1])
                Imagesz.image = a_images[current_index-1]
                ButtonSelect.config(command=lambda: select_item(mode='A')).place(relx=0.1, rely=0.9, anchor='s')
                ButtonDeselect.config(command=lambda: deselect_button(mode='A')).place(relx=0.1, rely=0.95, anchor='s')
                PlayaudioButton.config(command=lambda: play_audio(nmbr, mode='A'))
                PlayaudioButton.place(relx=0.98, rely=0.95, anchor='e')

            label2.pack()
            Imagesz.pack()
            if mode == 'G':
                GuestsButton.config(text="")
                GuestsButton.pack_forget()
            else:
                GuestsButton.config(text="Select Guests")
                GuestsButton.pack(side="bottom", padx=10, pady=5)
            if mode == 'F':
                FoodButton.config(text="")
                FoodButton.pack_forget()
            else:
                FoodButton.config(text="Select Tables")
                FoodButton.pack(side="bottom", padx=10, pady=5)
            if mode == 'A':
                AddonsButton.config(text="")
                AddonsButton.pack_forget()
            else:
                AddonsButton.config(text="Select Addons")
                AddonsButton.pack(side="bottom", padx=10, pady=5)



            BackvardButton.config(command=lambda: update_display(var, mode))
            BackvardButton.place(relx=0.01, rely=0.5, anchor='w')
            ForvardButton.config(command=lambda: update_display(nmbr+1, mode=mode))
            ForvardButton.place(relx=0.99, rely=0.5, anchor='e')

            if mode == 'G':
                ForvardButton.config(state="disabled") if nmbr == len(g_images) else ForvardButton.config(state="normal")
                BackvardButton.config(state="disabled") if nmbr == 1 else BackvardButton.config(state="normal")
            elif mode == 'F':
                ForvardButton.config(state="disabled") if nmbr == len(t_images) else ForvardButton.config(state="normal")
                BackvardButton.config(state="disabled") if nmbr == 1 else BackvardButton.config(state="normal")
            else:
                ForvardButton.config(state="disabled") if nmbr == a_status else ForvardButton.config(state="normal")
                BackvardButton.config(state="disabled") if nmbr == 1 else BackvardButton.config(state="normal")
            
        def deselect_button(mode='F'):
            if mode == 'F':
                #for each value in the dictionary, CHANGE ALL VALUES TO FALSE
                for key, value in self.types_of_tables.items():
                    self.types_of_tables[value] = not self.types_of_tables[value]
                    print(key, value)
                #make button disable
                ButtonDeselect.config(state="disabled")






        def select_item(mode='G'):
            current_index = int(status.cget("text").split(":")[1].split("/")[0]) - 1
            # Image shown
            imgpath = "Images/Oki.png"
            img2path = "Images/Nah.png"
            img = Image.open(imgpath)
            img2 = Image.open(img2path)
            img = img.resize((100, 100))
            img2 = img2.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            img2 = ImageTk.PhotoImage(img2)
            # Show the image
            label3 = tk.Label(self.root, font=("Helvetica", 16), fg="red", bg="#BAA391")
            label4 = tk.Label(self.root, image=img, background="#BAA391")
            label4.image = img
            label3.after(2000, lambda: label3.destroy())
            label4.after(2000, lambda: label4.destroy())

            if mode == 'F':
                #make button disable
               
                if self.types_of_tables[list(self.types_of_tables)[current_index]] == True:
                        ButtonSelect.config(state="disabled")
                #if all values are False, then the button will be 
               
                if ButtonSelect.winfo_exists():
                    ButtonSelect.pack_forget()
                if ButtonDeselect.winfo_exists():
                    ButtonDeselect.pack_forget()
                    

                for key, value in self.types_of_tables.items():
                    print(key, value)

                print("----------------------------------")
                self.types_of_tables[list(self.types_of_tables)[current_index]] = not self.types_of_tables[list(self.types_of_tables)[current_index]]

               
                

                print("----------------------------------")
                
                for key, value in self.types_of_tables.items():
                    print(key, value)

                    
                if  self.types_of_tables[list(self.types_of_tables)[current_index]] == True:
                    label3.config(text=f"{list(self.types_of_tables)[current_index]} is selected", fg="green")
                    label3.pack()                  
                    label4.pack()

                elif self.types_of_tables[list(self.types_of_tables)[current_index]] == False:
                    label3.config(text=f"{list(self.types_of_tables)[current_index]} is not selected")
                    label4.config(image=img2)
                    label4.image = img2
                    label3.pack()
                    label4.pack()
            elif mode == 'G':
                current_member = self.family_members[current_index]
                self.SelectGuest[current_member] = not self.SelectGuest[current_member]
                label3.config(text=f"{current_member} is not selected")
                if self.SelectGuest[current_member] == True:
                    label3.config(text=f"{current_member} is selected", fg="green")
                    label4.config(image=img)
                    label4.image = img
                    self.selected_guests.add(current_member)
                    if current_index < len(self.types_of_addons):
                        current_addon = self.types_of_addons[current_index]
                    else:
                        # Handle the case when current_index is out of range
                        current_addon = None
            elif mode == 'A':
                current_addon = self.types_of_addons[current_index]
                self.SelectAddon[current_addon] = not self.SelectAddon[current_addon]
                label3.config(text=f"{current_addon} is not selected")
                if self.SelectAddon[current_addon] == True:
                    label3.config(text=f"{current_addon} is selected", fg="green")
                    label4.config(image=img)
                    label4.image = img
                    self.selected_addons.add(current_addon)

   

        def __del__(self):
            # Destroy the application
            self.root.destroy()

    def selecting_guests(self,nmbr):

        if nmbr in self.SelectGuest:
            self.SelectGuest[nmbr] = not self.SelectGuest[nmbr]
            if self.SelectGuest[nmbr] == True:
                self.selected_guests.add(nmbr)
       

        # Create a frame for the guests
        
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


