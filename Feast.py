import tkinter as tk
import os
from PIL import ImageTk, Image
from platform import system
from sys import platform, version_info
from tkinter import PhotoImage, Button, Text, Scrollbar

class FeastApp: 
    def __init__(self):
        self.root = tk.Tk()
        self.initialize_window()

        self.load_images()
        self.initialize_descriptions()
        self.initialize_variables()
        self.initialize_ui()
        
    def initialize_window(self):
        self.root.title("Feast")
        self.root.configure(background="#BAA391")
        # Set the window icon based on the OS
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
        guests_paths = ["Images/Guests/Aunt_Vasilisa.jpeg", "Images/Guests/Dad_sis_Masha.jpeg", ...]
        tables_paths = ["Images/Table/FishyTable.jpeg", "Images/Table/MeatyTable.jpeg", ...]
        addons_paths = ["Images/addons/Auntie_tea.jpeg", "Images/addons/Beer.jpeg", ...]

        self.guests = {f"Guest{i}": Image.open(path) for i, path in enumerate(guests_paths, start=1)}
        self.tables = {f"Table{i}": Image.open(path) for i, path in enumerate(tables_paths, start=1)}
        self.addons = {f"Addon{i}": Image.open(path) for i, path in enumerate(addons_paths, start=1)}

        # Convert images to ImageTk format
        self.guest_images = {key: ImageTk.PhotoImage(image) for key, image in self.guests.items()}
        self.table_images = {key: ImageTk.PhotoImage(image) for key, image in self.tables.items()}
        self.addon_images = {key: ImageTk.PhotoImage(image) for key, image in self.addons.items()}
    def initialize_descriptions(self):
        file_path = "True Descriptions.txt"  # char description
        file_path2 = "Tables Description.txt"  # table description

        with open(file_path, 'r') as file:
            content = file.read()
        with open(file_path2, 'r') as file:
            content2 = file.read()

        descriptions = [desc.strip() for desc in content.split('- ') if desc.strip()]
        descriptions2 = [desc.strip() for desc in content2.split('- ') if desc.strip()]

        self.guest_descriptions = {
            self.family_members[i]: descriptions[i] for i in range(len(self.family_members))
        }
        self.table_descriptions = {
            self.types_of_tables[i]: descriptions2[i] for i in range(len(self.types_of_tables))
        }

    def initialize_variables(self):
        self.family_members = ["Vasilisa", "Masha", "Ludmila", "Boris", "Katya", "Olga", "Yaroslav", "Marzanna", "Gnevomir", "Borzena", "Zlata", "Mieszko"]
        self.SelectGuest = {member: False for member in self.family_members}

        self.types_of_tables = ["Fishy", "Meaty", "Vegan", "Vege"]
        self.SelectTable = {table: False for table in self.types_of_tables}

        self.types_of_addons = ["Auntie_tea", "Beer", "Honey", "Juices", "Lemon", "Salt", "Sugar", "Tea", "Vodka", "Wine"]
        self.SelectAddon = {addon: False for addon in self.types_of_addons}
    
    def initialize_ui(self):
        # Create labels for the title and instructions
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32), background="#BAA391")
        label1.pack()

        label2 = tk.Label(self.root, text="Please meet the family members and get to know them.", font=("Helvetica", 16), background="#BAA391")
        label2.pack()

        # Create an image label for the opening image
        opening_image = Image.open("Images/pierwsi.png")
        opening_image = ImageTk.PhotoImage(opening_image)
        image_label = tk.Label(image=opening_image)
        image_label.image = opening_image
        image_label.pack()

        # Create buttons for navigation
        forward_button = tk.Button(self.root, text=">>\n>>\n>>", command=lambda: self.update_display(1), font=("Helvetica", 20, 'bold'), bg="blue")
        forward_button.pack(side="right", padx=10, pady=10, anchor="e")

        backward_button = tk.Button(self.root, text="<<\n<<\n<<", command=lambda: self.update_display(), font=("Helvetica", 20, 'bold'), bg="red")
        backward_button.pack(side="left", padx=10, pady=10, anchor="w")

        continue_button = tk.Button(self.root, text="Continue", command=lambda: self.update_display(1, 'G'), font=("Helvetica", 20, 'bold'), bg="yellow")
        continue_button.pack(side="bottom", padx=10, pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Helvetica", 20, 'bold'), bg="green")
        exit_button.pack(side="bottom", padx=10, pady=10, anchor="s")

        # Other UI elements setup (status bar, etc.) if needed
        def update_display(self, nmbr, mode='F'):
            label1_text = "Please choose the type of food." if mode == 'F' else "Please meet the family members\nand get to know them."
            label1.config(text=label1_text)

            descriptions = self.table_descriptions if mode == 'F' else self.guest_descriptions
            description_index = nmbr - 1

            if mode == 'F':
                descriptions = list(self.table_descriptions.values())
                image_dict = self.table_images
            else:
                descriptions = list(self.guest_descriptions.values())
                image_dict = self.guest_images

            label2.config(text=descriptions[description_index])
            Imagesz.config(image=image_dict[f"Table{nmbr}"] if mode == 'F' else image_dict[f"Guest{nmbr}"])
            Imagesz.image = image_dict[f"Table{nmbr}"] if mode == 'F' else image_dict[f"Guest{nmbr}"]
            status.config(text=f"Status: {nmbr}/{len(descriptions)}")

            ButtonSelect.config(command=lambda: self.select_item(mode=mode))

            # ... Rest of the UI update logic for buttons and navigation
        def select_item(self, mode='F'):
            current_index = int(status.cget("text").split(":")[1].split("/")[0]) - 1

            if mode == 'F':
                current_table = self.types_of_tables[current_index]
                self.SelectTable[current_table] = not self.SelectTable[current_table]

                label_text = f"{current_table} is not selected"
                if self.SelectTable[current_table]:
                    label_text = f"{current_table} is selected"
                    label_color = "green"
                else:
                    label_color = "red"
            else:
                current_member = self.family_members[current_index]
                self.SelectGuest[current_member] = not self.SelectGuest[current_member]

                label_text = f"{current_member} is not selected"
                if self.SelectGuest[current_member]:
                    label_text = f"{current_member} is selected"
                    label_color = "green"
                else:
                    label_color = "red"

            label3.config(text=label_text, fg=label_color)

        def center_window(self, window):
            window.update_idletasks()
            width = window.winfo_width()
            frm_width = window.winfo_rootx() - window.winfo_x()
            win_width = width + 2 * frm_width
            height = window.winfo_height()
            titlebar_height = window.winfo_rooty() - window.winfo_y()
            win_height = height + titlebar_height + frm_width
            x = window.winfo_screenwidth() // 2 - win_width // 2
            y = window.winfo_screenheight() // 2 - win_height // 2
            window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            window.deiconify()
            
        def run(self):
            self.root.mainloop()

if __name__ == "__main__":
    app = FeastApp()
    app.center_window(app.root)
    app.run()



