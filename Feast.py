import tkinter as tk
import os
from PIL import ImageTk, Image
from platform import system
from sys import platform

class FeastApp:
    def __init__(self):
        self.root = tk.Tk()
        self.initialize_root()
        self.load_assets()
        self.create_variables()
        self.load_descriptions()
        self.center_window()

    def initialize_root(self):
        self.root.title("Feast")
        self.root.configure(background="#BAA391")
        icon_path = os.path.join(os.path.dirname(__file__), 'Icona.ico' if system() == 'Windows' else 'Icona.png')
        self.root.wm_iconbitmap(default=icon_path)
        self.root.resizable(False, False)

    def load_assets(self):
        self.guest_images, self.table_images, self.addon_images = {}, {}, {}
        self.load_image_set("Images/Guests/", self.guest_images)
        self.load_image_set("Images/Table/", self.table_images)
        self.load_image_set("Images/addons/", self.addon_images)

    def load_image_set(self, path, image_dict):
        image_paths = [os.path.join(path, file) for file in os.listdir(path)]
        images = {f"{os.path.splitext(os.path.basename(image))[0]}{i+1}": ImageTk.PhotoImage(Image.open(image))
            for i, image in enumerate(image_paths)}
        image_dict.update(images)

    def create_variables(self):
        self.family_members = ["Vasilisa", "Masha", "Ludmila", "Boris", "Katya", "Olga", "Yaroslav", "Marzanna", "Gnevomir", "Borzena", "Zlata", "Mieszko"]
        self.select_guest = {member: False for member in self.family_members}
        self.types_of_tables = ["Fishy", "Meaty", "Vegan", "Vege"]
        self.select_table = {table: False for table in self.types_of_tables}
        self.types_of_addons = ["Auntie_tea", "Beer", "Honey", "Juices", "Lemon", "Salt", "Sugar", "Tea", "Vodka", "Wine"]
        self.select_addon = {addon: False for addon in self.types_of_addons}

    def load_descriptions(self):
        self.guest_descriptions = self.read_description_file("True Descriptions.txt", self.family_members)
        self.table_descriptions = self.read_description_file("Tables Description.txt", self.types_of_tables)
        self.addon_descriptions = self.read_description_file("Addons Description.txt", self.types_of_addons)

    def read_description_file(self, file_path, items):
        with open(file_path, 'r') as file:
            content = file.read()
        descriptions = [desc.strip() for desc in content.split('* ') if desc.strip()]
        return descriptions[:len(items)]

    def gui(self):
        label1 = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32), background="#BAA391")
        label1.pack()

        opening_image = Image.open("Images/pierwsi.png")
        opening_image = ImageTk.PhotoImage(opening_image)
        images_label = tk.Label(image=opening_image)
        images_label.image = opening_image
        images_label.pack()

        label2 = tk.Label(self.root, text="Please meet the family members and get to know them.", font=("Helvetica", 14), background="#BAA391")
        label2.pack()

        status = tk.Label(self.root, text="Status: Start", font=("Helvetica", 20), bd=1, bg="#BAA391", relief='sunken', anchor='e')
        status.pack(side="bottom", fill="x")

        button_exit = tk.Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit, bg="green")
        button_exit.pack(side="bottom", padx=10, pady=5, anchor="s")

        button_select = tk.Button(self.root, text="Select", font=("Helvetica", 20, 'bold'), bg="green")
        guests_button = tk.Button(self.root, text="Select Guests", font=("Helvetica", 20, 'bold'), bg="yellow")

        def update_display(nmbr, mode='G'):
        nonlocal guests_button, button_select
        var = nmbr - 1
        g_status, t_status, a_status = len(self.guest_images), len(self.table_images), len(self.addon_images)

        if mode == 'F':
            label1.config(text="Please choose the type of food.")
            t_descriptions = list(self.table_descriptions.values())
            label2.config(text=t_descriptions[var])
            t_images = list(self.table_images.values())
            status.config(text=f"Status: {nmbr}/{t_status}")
            current_index = int(status.cget("text").split(":")[1].split("/")[0])
            button_select.config(command=lambda: select_item(mode='F'))
            images_label.config(image=t_images[current_index - 1])
            images_label.image = t_images[current_index - 1]
            status.config(text=f"Status: {nmbr}/{t_status}")
            button_select.config(command=lambda: select_item(mode='F'))
        elif mode == 'G':
            label1.config(text="Please meet the family members\n and get to know them.")
            g_descriptions = list(self.guest_descriptions.values())
            g_images = list(self.guest_images.values())
e Eleven Multil