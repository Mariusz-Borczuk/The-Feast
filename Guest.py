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
    """

    # Default values for attributes
    name = "Guest"
    isPicked = False
    title = "Guest"
    description = "This is a guest"
    status = "Alive"
    location = "Unknown"

    # Class-level attributes to hold titles and descriptions
    titles = []
    descriptions = []

    def __init__(self, id: int) -> None:
        self.id = id   # Adjust id to be 0-indexed

        # Load data if not already loaded
        if not Guest.titles or not Guest.descriptions:
            self.load_data()

        # Assign the descriptions to the guest based on the id
        if 0 <= self.id < len(Guest.titles) and 0 <= self.id < len(Guest.descriptions):
            self.title = Guest.titles[self.id]
            self.description = Guest.descriptions[self.id]
        else:
            self.title = "Guest"
            self.description = "This is a guest"

    @classmethod
    def load_data(cls):
        """
        Load the titles and descriptions from the files.
        """
        title_path = "Feast_txts/Guests_Titles.txt"
        description_path = "Feast_txts/Guests_Descriptions.txt"

        try:
            with open(title_path, 'r') as file:
                cls.titles = [title.strip() for title in file.read().split('* ') if title.strip()]
            with open(description_path, 'r') as file:
                cls.descriptions = [desc.strip() for desc in file.read().split('* ') if desc.strip()]
        except FileNotFoundError as e:
            print(f"Error: {e}")
            cls.titles = []
            cls.descriptions = []

    @classmethod
    def get_all_guests(cls, num_guests: int = 11) -> list:
        """
        Return a list of all guests.
        
        Parameters
        ----------
        num_guests : int
            Number of guests to retrieve, default is 11.

        Returns
        -------
        list
            list of all guests
        """
        guests = []
        for i in range(1, num_guests + 1):
            guest = cls(i)
            guests.append(guest)
        return guests

    def __str__(self):
        return f"name: {self.name}, title: {self.title}, description: {self.description}, status: {self.status}, location: {self.location}"
    def __repr__(self):
        return f"<Guest id={self.id}, title='{self.title}', description='{self.description}'>"

if __name__ == "__main__":
    all_guests = Guest.get_all_guests()
        