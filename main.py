import os
import Guest
import Table
import Addon
import pygame
import traceback
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

        # @change
        self.create_variables()

        self.gui()
        self.center_window(self.root)

    def inizialize_root(self):  # Initialize is perfect
        """  Initializes the root window with the title and Background."""
        self.root.title("Feast")
        ## TEST
        # self.root.configure(background="#BAA391")

        # Use image as a background for the window
        bg_image = Image.open("Images/BG2.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

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

    @staticmethod
    def create_variables():  #
        """ Initialises variables from other files."""
        # Loading Guests
        guests: [] = Guest.Guest.get_all_guests()
        print(guests[0].name)
        # Loading Tables
        tables: [] = Table.Table.get_all_food()
        # Loading Addons
        addons: [] = Addon.Addon.get_all_addons()

    def gui(self):
        """ Graphical Interface of the game"""

        # First label for the title
        huge_title = tk.Label(self.root, text="Welcome to The Feast paragraph game!", font=("Helvetica", 32),
                              background="#BAA391")

        huge_title.pack()

        # Create an entry image on top of the Background
        opening_image = Image.open("Images/pierwsi.png")
        opening_image = ImageTk.PhotoImage(opening_image)
        image_form = tk.Label(image=opening_image)
        image_form.image = opening_image
        image_form.pack()

        # title_label for the description
        title_label = tk.Label(self.root, text="Description", font=("Helvetica", 20), background="#BAA391")
        title_label.pack()

        # Second label for the description
        body_label = tk.Label(self.root, text="Please meet the family members and get to know them.",
                              font=("Helvetica", 14), background="#BAA391")
        body_label.pack()

        # Create buttons for navigation 
        nmbr = 1  # Define the variable "nmbr"
        mode = 'G'  # Define the variable "mode"

        # Navigation buttons
        forvard_button = Button(self.root, text=">>\n>>\n>>", command=lambda: update_display(1),
                                font=("Helvetica", 20, 'bold'), bg="blue")
        backvard_button = Button(self.root, text="<<\n<<\n<<", command=lambda: update_display(0),
                                 font=("Helvetica", 20, 'bold'), bg="red")

        # Audio button
        play_audio_button = Button(self.root, text="Play audio", font=("Helvetica", 20, 'bold'),
                                   command=lambda: play_audio(nmbr, mode), bg="yellow")

        # Status bar
        status_label = tk.Label(self.root, text="Status: Start", font=("Helvetica", 20), bd=1, bg="#BAA391",
                                relief='sunken', anchor='e')
        status_label.pack(side="bottom", fill="x")

        # Exit button
        exit_button = Button(self.root, text="Exit", font=("Helvetica", 20, 'bold'), command=self.root.quit,
                             bg="green")
        exit_button.pack(side="bottom", padx=10, pady=5, anchor="s")

        # Select button
        select_button = Button(self.root, text="Select", font=("Helvetica", 20, 'bold'),
                               command=lambda: select_item(mode='G'), bg="green")
        select_button.place(relx=0.1, rely=0.9, anchor='s')

        # Deselect button
        # deselect_button = Button(self.root, text="Deselect", font=("Helvetica", 20, 'bold'),
        #                        command=lambda: deselect_button(mode='F'), bg="red")
        # deselect_button.place(relx=0.1, rely=0.95, anchor='s')

        # Food button
        foods_button = Button(self.root, text="Select Tables", font=("Helvetica", 20, 'bold'),
                              command=lambda: update_display(1, mode='F'), bg="yellow")
        foods_button.pack(side="bottom", padx=10, pady=5)

        # Guests button
        guests_button = Button(self.root, text="Select Guests", font=("Helvetica", 20, 'bold'),
                               command=lambda: update_display(1), bg="yellow")
        guests_button.pack(side="bottom", padx=10, pady=5)

        # Addons button
        addons_button = Button(self.root, text="Select Addons", font=("Helvetica", 20, 'bold'),
                               command=lambda: update_display(1, mode='A'), bg="yellow")
        addons_button.pack(side="bottom", padx=10, pady=5)

        def determine_audio_path(nmbr: int, mode: str):
            """
            Determines the path to the audio file based on the given mode and number.

            :param nmbr: The number associated with the audio file.
            :type nmbr: int
            :param mode: The mode determining the category of the audio file ('G' for guests, 'F' for tables, others for addons).
            :type mode: str
            :return: The path to the audio file.
            :rtype: str
            """

            audio_paths_guests = ["Audio/V.wav", "Audio/Mas.wav", "Audio/Lu.wav", "Audio/Br.wav",
                                  "Audio/Ka.wav", "Audio/Ol.wav", "Audio/Ya.wav", "Audio/Ma.wav",
                                  "Audio/Gn.wav", "Audio/Bo.wav", "Audio/Zl.wav", "Audio/Mi.wav"]

            audio_paths_tables = ["Audio/Fish.mp3", "Audio/Meat.mp3", "Audio/Vegan.mp3", "Audio/Vege.mp3"]

            audio_paths_addons = ["Audio/Vastea.mp3", "Audio/Beer.mp3", "Audio/Honey.mp3", "Audio/Juices.mp3",
                                  "Audio/Lemon.mp3", "Audio/Salt.mp3", "Audio/Sugar.mp3", "Audio/Tea.mp3",
                                  "Audio/Vodka.mp3", "Audio/Vine.mp3"]

            # @change
            # Create a dictionary to map modes to lists
            mode_to_paths = {
                'G': audio_paths_guests,
                'F': audio_paths_tables,
                'A': audio_paths_addons  # Assuming 'A' or any other character is used for addons
            }
            # Get the corresponding list based on the mode
            audio_paths = mode_to_paths.get(mode, mode_to_paths['A'])

            # Validate the number
            if 1 <= nmbr <= len(audio_paths):
                return audio_paths[nmbr - 1]
            else:
                raise ValueError(f"Number {nmbr} is out of range for the selected mode '{mode}'")
                if mode not in ['G', 'F', 'A']:
                    raise ValueError("Invalid mode")

        def play_audio(nmbr: int, mode: str):
            """ Plays the audio file based on the given number and mode.

            :param nmbr: The number associated with the audio file.
            :type nmbr: int
            :param mode: The mode determining the category of the audio file ('G' for guests, 'F' for tables, 'A' or others for addons).
            :type mode: str
            """
            mixer.init()
            try:
                audio_path = determine_audio_path(nmbr, mode)
                mixer.music.load(audio_path)
                mixer.music.play()

            except FileExistsError:
                print(f"Error: File {audio_path} does not exist.")
            except pygame.error as pygame_err:
                print(f"Error initializing or playing audio with pygame: {pygame_err}")
            except Exception as e:
                print(f"An unexpected error occurred while playing audio.")
                print(f"Parameters - nmbr: {nmbr}, mode: {mode}")
                print(f"Error message: {e}")
                print("Traceback:")
                traceback.print_exc()

        def update_display(nmbr: int, mode: str = 'G'):  # @changed
            """
            Updates the display of the application through every iteration of pages.

            This function dynamically updates the UI components based on the current mode and
            page number. It handles the display of descriptions, images, and fronter for different
            modes ('G' for guests, 'F' for food/tables, and 'A' for addons), and configures
            navigation and action buttons accordingly.

            Parameters:
            nmbr (int): The current page number to display.
            mode (str): The mode of the application, which determines the type of content to display.
                        Default is 'G' for guests.

            Functionality:
            - Updates the title based on the current mode.
            - Displays the current status as "Status: current_page/total_pages".
            - Updates the body label with the corresponding description for the current page.
            - Displays the appropriate image for the current page.
            - Configures the action buttons (select, deselect, play audio) with their respective commands.
            - Places the action buttons at specified positions.
            - Shows or hides the mode selection buttons (guests, food, addons) based on the current mode.
            - Configures the mode selection buttons with appropriate text.
            - Configures the navigation buttons (back and forward) with their respective commands.
            - Enables or disables the navigation buttons based on the current index.

            Note:
            - The function assumes that self.guests, self.tables, self.addons, self.guest_descriptions,
            self.table_descriptions, self.addon_descriptions, self.guest_images, self.table_images,
            and self.addon_images are pre-populated dictionaries containing relevant data.
            - Button and label widgets like huge_title, status_label, body_label, image_form, select_button,
            deselect_button, play_audio_button, guests_button, foods_button, addons_button, backvard_button,
            and forvard_button are assumed to be pre-defined within the class.
            """

            var = nmbr - 1
            status_labels = {
                'G': len(self.guests),
                'F': len(self.tables),
                'A': len(self.addons)
            }

            descriptions = {
                'G': list(self.guests.description),
                'F': list(self.tables.description),
                'A': list(self.addons.description)
            }

            images = {
                'G': list(self.guest.image),
                'F': list(self.table.image),
                'A': list(self.addon.image)
            }

            fronter = {
                'G': "Please meet the family members\n and get to know them.",
                'F': "Please choose the type of food.",
                'A': "Please choose the addons up to 6."
            }

            huge_title.config(text=fronter[mode])

            # Update labels and images
            status_label.config(text=f"Status: {nmbr}/{status_labels[mode]}")
            current_index = int(status_label.cget("text").split(":")[1].split("/")[0])
            body_label.config(text=descriptions[mode][var])
            image_form.config(image=images[mode][current_index - 1])
            image_form.image = images[mode][current_index - 1]

            # Configure buttons
            select_button.config(command=lambda: select_item(mode=mode))
            # deselect_button.config(command=lambda: deselect_item(mode=mode))
            play_audio_button.config(command=lambda: play_audio(nmbr, mode=mode))

            select_button.place(relx=0.1, rely=0.9, anchor='s')
            # deselect_button.place(relx=0.1, rely=0.95, anchor='s')
            play_audio_button.place(relx=0.99, rely=0.95, anchor='e')

            # Show or hide buttons based on mode
            guests_button.pack_forget() if mode == 'G' else guests_button.pack(side="bottom", padx=10, pady=5)
            foods_button.pack_forget() if mode == 'F' else foods_button.pack(side="bottom", padx=10, pady=5)
            addons_button.pack_forget() if mode == 'A' else addons_button.pack(side="bottom", padx=10, pady=5)

            guests_button.config(text="" if mode == 'G' else "Select Guests")
            foods_button.config(text="" if mode == 'F' else "Select Tables")
            addons_button.config(text="" if mode == 'A' else "Select Addons")

            # Configure navigation buttons
            backvard_button.config(command=lambda: update_display(var, mode))
            forvard_button.config(command=lambda: update_display(nmbr + 1, mode=mode))

            backvard_button.place(relx=0.01, rely=0.5, anchor='w')
            forvard_button.place(relx=0.99, rely=0.5, anchor='e')

            # Enable/disable navigation buttons based on the current index
            if mode in ['G', 'F']:
                total_items = len(images[mode])
            else:
                total_items = status_labels[mode]

            forvard_button.config(state="normal" if nmbr != total_items else "disabled")
            backvard_button.config(state="normal" if nmbr > 1 else "disabled")

        # def deselect_button(mode: str = 'F'):
        #     if mode == 'F': # ?
        #         # for each value in the dictionary, CHANGE ALL VALUES TO FALSE
        #         for key, value in self.types_of_tables.items():
        #             self.types_of_tables[value] = not self.types_of_tables[value]
        #             print(key, value)
        #         #make button disable
        #         deselect_button.config(state="disabled")

        def select_item(mode: str = 'G'):
            """ Selecting the image and showing it was done via showing image
            :type mode: object
            """
            current_index = int(status_label.cget("text").split(":")[1].split("/")[0]) - 1
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
                # make button disable

                if self.types_of_tables[list(self.types_of_tables)[current_index]]:
                    select_button.config(state="disabled")
                # if all values are False, then the button will be

                if select_button.winfo_exists():
                    select_button.pack_forget()
                # if deselect_button.winfo_exists():
                # deselect_button.pack_forget()

                for key, value in self.types_of_tables.items():
                    print(key, value)

                print("----------------------------------")
                self.types_of_tables[list(self.types_of_tables)[current_index]] = not self.types_of_tables[
                    list(self.types_of_tables)[current_index]]

                print("----------------------------------")

                for key, value in self.types_of_tables.items():
                    print(key, value)

                if self.types_of_tables[list(self.types_of_tables)[current_index]]:
                    label3.config(text=f"{list(self.types_of_tables)[current_index]} is selected", fg="green")
                    label3.pack()
                    label4.pack()

                elif not self.types_of_tables[list(self.types_of_tables)[current_index]]:
                    label3.config(text=f"{list(self.types_of_tables)[current_index]} is not selected")
                    label4.config(image=img2)
                    label4.image = img2
                    label3.pack()
                    label4.pack()
            elif mode == 'G':
                current_member = self.family_members[current_index]
                self.SelectGuest[current_member] = not self.SelectGuest[current_member]
                label3.config(text=f"{current_member} is not selected")
                if self.SelectGuest[current_member]:
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
                if self.SelectAddon[current_addon]:
                    label3.config(text=f"{current_addon} is selected", fg="green")
                    label4.config(image=img)
                    label4.image = img
                    self.selected_addons.add(current_addon)

        # def __del__(self):
        # Destroy the application
        #   self.root.destroy()

    @staticmethod
    def center_window(root):
        """
        Centers the application window in the middle of the screen.

        This function calculates the appropriate x and y coordinates to position the window
        in the center of the screen based on the operating system. It handles both Linux and
        Windows OS to ensure the window is centered correctly.

        Parameters:
        root (tk.Tk): The root window instance of the Tkinter application.
        """
        # Set the desired window size
        width, height = 980, 1080

        # Get the screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the position coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # Adjust y position for Windows
        if platform == "Windows":
            y = (screen_height / 2) - (height / 1.9)

        # Set the geometry of the window
        root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def run(self):
        # Run the application
        self.root.mainloop()


if __name__ == "__main__":
    app = FeastApp()

    app.center_window(app.root)
    app.run()
