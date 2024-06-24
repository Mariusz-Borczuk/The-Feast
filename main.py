import os
import Guest2
import tkinter as tk
from pygame import mixer
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
      


        
    def inizialize_root(self): #Initialize is perfect
        # Initialize the root window with the title and Background
        self.root.title("Feast")
        ##TEST
        #self.root.configure(background="#BAA391")

        # Use image as a background for the window
        bg_image = Image.open("Images/BG2.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo
        
        # Set the icon for the application depending on the operating system
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

    def load_images(self): #Load is pretty
        try:
            # Define the paths to the images //@Upgrade
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
        
        except IOError as e:
            # Handle file not found or other IO errors
            print(f"Error loading images: {e}")
            # Optionally, set default images or handle error state

        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"Unexpected error loading images: {e}")
            # Optionally, set default images or handle error state
    
    def Create_variables(self): #
        
        if __name__ == "__main__":
        
          Guest.Guest.main()

    def Gui_(self):

        ##Labels
        # First label for the title
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32),background="#BAA391")
                #Audio here
        label1.pack() 

        # Create an entry image on top of the Background
        OpeningImage = Image.open("Images/pierwsi.png")
        OpeningImage = ImageTk.PhotoImage(OpeningImage)
        Imagesz = tk.Label(image=OpeningImage)     
        Imagesz.image = OpeningImage
        Imagesz.pack()  

        # Title for the description
        Title = tk.Label(self.root, text="Description", font=("Helvetica", 20),background="#BAA391")
        Title.pack()

        # Second label for the description
        Body = tk.Label(self.root, text="Please meet the family members and get to know them." , font=("Helvetica", 14),background="#BAA391")
        Body.pack()   
        
        ##Buttons
        # Create buttons for navigation 
        nmbr = 1  # Define the variable "nmbr"
        mode = 'G'  # Define the variable "mode"
        
        # Navigation buttons
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
            list_of_audio_paths_guests = ["Audio/V.wav","Audio/Mas.wav","Audio/Lu.wav","Audio/Br.wav","Audio/Ka.wav","Audio/Ol.wav","Audio/Ya.wav","Audio/Ma.wav","Audio/Gn.wav","Audio/Bo.wav","Audio/Zl.wav","Audio/Mi.wav"]
            list_of_audio_paths_tables = ["Audio/Fish.mp3", "Audio/Meat.mp3", "Audio/Vegan.mp3", "Audio/Vege.mp3"]
            list_of_audio_paths_addons = ["Audio/Vastea.mp3", "Audio/Beer.mp3", "Audio/Honey.mp3", "Audio/Juices.mp3", "Audio/Lemon.mp3", "Audio/Salt.mp3", "Audio/Sugar.mp3", "Audio/Tea.mp3", "Audio/Vodka.mp3", "Audio/Vine.mp3"]
           
           # Return the path to the audio file 
            if mode == 'G':
                return list_of_audio_paths_guests[nmbr-1]
            elif mode == 'F':
                return list_of_audio_paths_tables[nmbr-1]
            else:
                return list_of_audio_paths_addons[nmbr-1]
        
        def play_audio(nmbr, mode):
            # Play the audio file @change to my own player 
            audio_path = determine_audio_path(nmbr, mode)
            print(audio_path)
            mixer.init()
            mixer.music.load(audio_path)
            mixer.music.play()
            
        def update_display(nmbr, mode='G'):
            # Update the display of the application through every iteration of pages
            var = nmbr - 1
            g_status = len(self.guests.values())
            t_status = len(self.tables.values())
            a_status = len(self.addons.values())

            if mode == 'F':
                label1.config(text="Please choose the type of food.")
                #Audio here @Add
                
                # Get the descriptions and images
                t_descriptions = list(self.table_descriptions.values())
                t_images = list(self.table_images.values())
                
                # Assign the description and image to the corresponding variables
                Title
                Body.config(text=t_descriptions[var])
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
                #Audio here @Add
                
                # Get the descriptions and images
                g_descriptions = list(self.guest_descriptions.values())
                g_images = list(self.guest_images.values())
                status.config(text=f"Status: {nmbr}/{g_status}")
                current_index = int(status.cget("text").split(":")[1].split("/")[0])
                Body.config(text=g_descriptions[var])
                Imagesz.config(image=g_images[current_index-1])
                Imagesz.image = g_images[current_index-1]
                PlayaudioButton.config(command=lambda: play_audio(nmbr, mode='G'))
                PlayaudioButton.place(relx=0.99, rely=0.95, anchor='e')
                ButtonSelect.config(command=lambda: select_item(mode='G'))
                ButtonSelect.place(relx=0.1, rely=0.9, anchor='s')
                ButtonDeselect.config(command=lambda: deselect_button(mode='G'))
                ButtonDeselect.place(relx=0.1, rely=0.95, anchor='s')
            elif mode == 'A':
                label1.config(text="Please choose the addons up to 6.")
                #Audio here @Add

                # Get the descriptions and images
                a_descriptions = list(self.addon_descriptions.values())
                a_images = list(self.addon_images.values())
                status.config(text=f"Status: {nmbr}/{a_status}")
                current_index = int(status.cget("text").split(":")[1].split("/")[0])
                Body.config(text=a_descriptions[var])
                Imagesz.config(image=a_images[current_index-1])
                Imagesz.image = a_images[current_index-1]
                ButtonSelect.config(command=lambda: select_item(mode='A'))
                ButtonSelect    .place(relx=0.1, rely=0.9, anchor='s')
                ButtonDeselect.config(command=lambda: deselect_button(mode='A'))
                ButtonDeselect.place(relx=0.1, rely=0.95, anchor='s')
                PlayaudioButton.config(command=lambda: play_audio(nmbr, mode='A'))
                PlayaudioButton.place(relx=0.98, rely=0.95, anchor='e')
                Body.pack()
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
            width,height = 980, 1080
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


