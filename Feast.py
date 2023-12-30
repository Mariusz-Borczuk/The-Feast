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
        

        # Create a label for the title
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32),background="#BAA391")
        label1.pack()        
        # Create a label for instructions
        label2 = tk.Label(self.root, text="Please meet the family members and get to know them." , font=("Helvetica", 16),background="#BAA391")
        label2.pack()     

# Images
        
        #make buttons smaller
        OpeningImage = Image.open("Images/pierwsi.png")
        list_of_paths_Guests = ["Images/Guests/Aunt_Vasilisa.jpeg", "Images/Guests/Dad_sis_Masha.jpeg", "Images/Guests/Luba_Ludmila.jpeg", "Images/Guests/BF_Boris.jpeg", "Images/Guests/BF_Katya.jpeg", "Images/Guests/Cousin_Olga.jpeg", "Images/Guests/Dad_Yaroslav.jpeg", "Images/Guests/Grandma_Marzanna.jpeg", "Images/Guests/Grandpa_Gnevomir.jpeg", "Images/Guests/Mom_Borzena.jpeg", "Images/Guests/Sis_Zlata.jpeg", "Images/Guests/Uncle_Mieszko.jpeg"]
        list_of_paths_Tables = ["Images/Table/FishyTable.jpeg", "Images/Table/MeatyTable.jpeg", "Images/Table/VeganTable.jpeg", "Images/Table/VegeTable.jpeg"]
        list_of_paths_Addons = ["Images/addons/Auntie_tea.jpeg", "Images/addons/Beer.jpeg", "Images/addons/Honey.jpeg", "Images/addons/Juices.jpeg", "Images/addons/Lemon.jpeg", "Images/addons/Salt.jpeg", "Images/addons/Sugar.jpeg", "Images/addons/Tea.jpeg", "Images/addons/Vodka.jpeg", "Images/addons/Wine.jpeg"]
        # Create a dictionary of images
        guests, addons, tables={}, {}, {}
        
#reading images
        #read from list Guests 1-12 and write it to variable make them in order
        for i ,path in enumerate(list_of_paths_Guests, start=1):
             guests[f"Guest{i}"] = Image.open(path)
        #read from list Tables 1-4 and write it to variable make them in order
        for i ,path in enumerate(list_of_paths_Tables, start=1):
            tables[f"Table{i}"] = Image.open(path)
        #read from list addons 1-10 and write it to variable make them in order
        for i ,path in enumerate(list_of_paths_Addons, start=1):
            addons[f"Addon{i}"] = Image.open(path)
                   
#assigning images to variables   
       #ImageTk for guests
        for i in guests:
            guests[i] = ImageTk.PhotoImage(guests[i])
        #ImageTk for tables
        for i in tables:
            tables[i] = ImageTk.PhotoImage(tables[i])
        #ImageTk for addons
        for i in addons:
            addons[i] = ImageTk.PhotoImage(addons[i])
        #ImageTk for buttons
        OpeningImage = ImageTk.PhotoImage(OpeningImage)
        Imagesz = tk.Label(image=OpeningImage)     
        Imagesz.image = OpeningImage
        Imagesz.pack()
        
# Descriptions
        file_path = "True Descriptions.txt"  # Replace with the actual path to your text file

        with open(file_path, 'r') as file:
            content = file.read()

        # Split the content into individual descriptions
        descriptions = content.split('- ')
        
#Variables to use later Guests
        self.family_members = ["Vasilisa", "Masha", "Ludmila", "Boris", "Katya", "Olga", "Yaroslav", "Marzanna", "Gnevomir", "Borzena", "Zlata", "Mieszko"]
        self.SelectGuest = {member: False for member in self.family_members}

        self.types_of_tables = ["Fishy", "Meaty", "Vegan", "Vege"]
        self.SelectTable = {table: False for table in self.types_of_tables}

        self.types_of_addons = ["Auntie_tea", "Beer", "Honey", "Juices", "Lemon", "Salt", "Sugar", "Tea", "Vodka", "Wine"]
        self.SelectAddon = {addon: False for addon in self.types_of_addons}

# Remove empty strings and leading/trailing whitespace
        descriptions = [desc.strip() for desc in descriptions if desc.strip()]
        # Assign each description to a variable
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
        # Create a status bar
        status = tk.Label(self.root, text="Status: Start",font= ("Helvetica",20) , bd=1,bg="#BAA391", relief='sunken', anchor='e')
        status.pack(side="bottom", fill="x")
        
# Create functions
        def update_display(nmbr):
            # Update labels and image
            label1.config(text="Please meet the family members\n and get to know them.")
            label2.config(text=descriptions[nmbr - 1])
            Imagesz.config(image=guests[f"Guest{nmbr}"])
            Imagesz.image = guests[f"Guest{nmbr}"]
            # Pack labels and image
            label2.pack()
            Imagesz.pack()
            # Update status label
            status.config(text=f"Status: {nmbr}/{len(descriptions)}")
            # Hide the ContinueButton
            ContinueButton.config(text="")
            ContinueButton.pack_forget()
            # Configure Backward Button
            BackvardButton.config(command=lambda: update_display(nmbr - 1))
            BackvardButton.pack(side="left", padx=10, pady=10, anchor="w")
            # Configure Forward Button
            ForvardButton.config(command=lambda: update_display(nmbr + 1))
            ForvardButton.pack(side="right", padx=10, pady=10, anchor="e")
            # Disable Forward Button when reaching the last family member
            ForvardButton.config(state="disabled") if nmbr == len(descriptions) else ForvardButton.config(state="normal")
            # Disable Backward Button when at the first family member
            BackvardButton.config(state="disabled") if nmbr == 1 else BackvardButton.config(state="normal")

        def Guest_select():
            # Get the current family member
            current_index = int(status.cget("text").split(":")[1].split("/")[0]) - 1
            current_member = self.family_members[current_index]
            # Toggle the boolean value for the current family member
            self.SelectGuest[current_member] = not self.SelectGuest[current_member]
            imgpath = "Images/Oki.jpeg"
            img2path = "Images/Nah.jpeg"
            img = Image.open(imgpath)
            img2 = Image.open(img2path)
            #resize the image
            img = img.resize((100, 100))
            img2 = img2.resize((100, 100))
            img = ImageTk.PhotoImage(img)
            img2 = ImageTk.PhotoImage(img2)
            # Update the Selection label
            label3 = tk.Label(self.root, text=f"{current_member} is not selected", font=("Helvetica", 16),fg="red",bg="#BAA391")
            label3.pack()
            # Update the Selection label
            label4 = tk.Label(self.root, image=img2,background="#BAA391")
            label4.image = img2
            label4.pack()
            # Destroy the Selection label after 2 seconds
            label3.after(2000, lambda: label3.destroy())
            label4.after(2000, lambda: label4.destroy())
            # Update the ContinueButton
            if self.SelectGuest[current_member] == True:
                label3.config(text=f"{current_member} is selected", fg="green")
                label4.config(image=img)
                label4.image = img
                
# Buttons
        # Create buttons for navigation 
        ForvardButton = Button(self.root, text=">>\n>>\n>>", command=lambda: update_display(1), font=("Helvetica", 20, 'bold'), bg="blue")
        BackvardButton = Button(self.root, text="<<\n<<\n<<",command= lambda: update_display(), font=("Helvetica", 20, 'bold'), bg="red")
        # Exit button
        ButtonExit = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green").pack(side="bottom", padx=10, pady=10, anchor="s")
        # Select button
        ButtonSelect = Button(self.root, text="Select",command= Guest_select , font=("Helvetica", 20, 'bold'), bg="green").pack(side="bottom", padx=10, pady=10, anchor="s")
        ButtonNext = Button(self.root, text="Next", font=("Helvetica", 20, 'bold'), command=self.nextParagraph, bg="yellow").pack(side="bottom", padx=10, pady=10, anchor="s")
        # Continue button
        ContinueButton = Button(self.root, text="Continue", font=("Helvetica", 20, 'bold'), command=lambda:update_display(1), bg="yellow")
        ContinueButton.pack( side="bottom",padx=10, pady=10)

        def __del__(self):
            # Destroy the application
            self.root.destroy()
        
# Create definitions of methods
    def nextParagraph(nmbr):
        if nmbr == 1:
            label1.config(text="Please choose the type of table dishes.")
            label2.config(text=descriptions[nmbr - 1])
            Imagesz.config(image=guests[f"Guest{nmbr}"])
            Imagesz.image = guests[f"Guest{nmbr}"]
           
        
    def center_window(self, root):
            width,height = 980, 1000
            screen_width,screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
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



