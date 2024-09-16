from PIL import ImageTk, Image


class Guest:
    """ 
    A class to represent a guest in the game.

    Attributes
    ----------
    id : int
        the id of the guest
    name : str
        the name of the guest
    isPicked : bool
        whether the guest is isPicked    
    title : str
        the title of the guest
    description : str
        the description of the guest
    status : str
        the status of the guest
    location : str
        the location of the guest
    image_path : str
        the photo of the guest
    image : object
        the image of the guest
    """

    # Default values for attributes
    name = "Guest"
    isPicked = False
    title = "Guest"
    description = "This is a guest"
    status = "Alive"
    location = "Unknown"
    image_path = "Images/Guests/Unknown.png"
    image = None

    # Class-level attributes to hold titles and descriptions
    names: tuple = ()
    titles: tuple = ()
    descriptions: tuple = ()
    image_paths: tuple = ()
    images: tuple = ()
    imagesTk: tuple = ()

    def __init__(self, id: int) -> None:
        """

        :type id: object
        """
        self.id = id  # Adjust id to be 0-indexed

        # Load data if not already loaded
        if not Guest.titles or not Guest.descriptions or not Guest.image_paths or not Guest.names:
            self.load_data()
            self.load_images()

        # Assign the descriptions to the guest based on the id
        if 0 <= self.id < len(Guest.titles) and 0 <= self.id < len(Guest.names) and 0 <= self.id < len(
            Guest.descriptions) and 0 <= self.id < len(Guest.image_paths):
            #
            self.title = Guest.titles[self.id]
            self.description = Guest.descriptions[self.id]
            self.image_path = Guest.image_paths[self.id]

            self.name = Guest.names[self.id]
            if 0 <= self.id < len(Guest.imagesTk):
                self.image = Guest.imagesTk[self.id]

        else:
            self.name = "idiot"
            self.title = "Guest"
            self.description = "This is a guest"
            self.image_path = "Images/Guests/Unknown.png"
            self.image = None

    @classmethod
    def load_data(cls):
        """
        Load the titles and descriptions from the files.
        """
        title_path = "Feast_txts/Guests_Titles.txt"
        description_path = "Feast_txts/Guests_Descriptions.txt"
        name_path = "Feast_txts/Guests_Names.txt"

        try:
            with open(title_path, 'r') as file:
                cls.titles = [title.strip() for title in file.read().split('* ') if title.strip()]
            with open(name_path, 'r') as file:
                cls.names = [name.strip() for name in file.read().split('* ') if name.strip()]
            with open(description_path, 'r') as file:
                cls.descriptions = [desc.strip() for desc in file.read().split('* ') if desc.strip()]
        except FileNotFoundError as e:
            print(f"Error: {e}")
            cls.titles = ()
            cls.descriptions = ()
            cls.names = ()
        except Exception as e:
            print(f"Error: {e}")
            cls.titles = ()
            cls.descriptions = ()
            cls.names = ()

    @classmethod
    def load_images(cls) -> None:  # Load is pretty
        """
            Loading images //can e initialized to object as a built in attribute
            """
        try:

            guests_paths = ["Images/Guests/Aunt_Vasilisa.png", "Images/Guests/Dad_sis_Masha.png",
                            "Images/Guests/Luba_Ludmila.png", "Images/Guests/BF_Boris.png",
                            "Images/Guests/BF_Katya.png", "Images/Guests/Cousin_Olga.png",
                            "Images/Guests/Dad_Yaroslav.png", "Images/Guests/Grandma_Marzanna.png",
                            "Images/Guests/Grandpa_Gnevomir.png", "Images/Guests/Mom_Borzena.png",
                            "Images/Guests/Sis_Zlata.png", "Images/Guests/Uncle_Mieszko.png"]

            # Assign the Images to the guest for each guest
            cls.image_paths = guests_paths
            cls.images = (Image.open(image_path) for image_path in cls.image_paths)
            cls.imagesTk = (ImageTk.PhotoImage(image) for image in cls.images)


        # Make images a class attribute
        except IOError as e:
            # Handle file not found or other IO errors
            print(f"Error loading images: {e}")
            # Optionally, set default images or handle error state

        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"Unexpected error loading images: {e}")
            # Optionally, set default images or handle error state

    @classmethod
    def get_all_guests(cls, num_guests: int = 11) -> tuple:
        """
        Return a tuple of all guests.
        
        Parameters
        ----------
        num_guests : int
            Number of guests to retrieve, default is 11.

        Returns
        -------
        tuple
            tuple of all guests
        """
        guests: tuple = ()
        for i in range(0, num_guests + 1):
            guest = cls(i)
            guests += (guest,)
        return guests

    def __str__(self):
        return f"name: {self.name}, title: {self.title}, description: {self.description}, status: {self.status}, location: {self.location}"

    def __repr__(self):
        return f"<Guest id={self.id}, name={self.name}, title='{self.title}', description='{self.description}, image_path='{self.image_path}, image='{self.image}'>\n\n"


if __name__ == "__main__":
    all_guests: tuple = Guest.get_all_guests()
    print(all_guests)
