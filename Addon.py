class Addon:
    """
    A class to represent an addon
    
    Attributes
    ----------
    id : int
        the id of the addon
    name : str
        the name of the addon
    isPicked : bool
        whether the addon is isPicked
    amount : int
        the amount of the addon
    title : str
        the title of the addon
    description : str
        the description of the addon
    """

    # Default values for attributes
    name = "Addon"
    isPicked = False
    amount = 0
    title = "Addon"
    description = "This is an addon"

    # Class-level attributes to hold titles and descriptions
    titles = []
    descriptions = []

    def __init__(self, id: int) -> None:
        self.id = id

        # Load data if not already loaded
        if not Addon.titles or not Addon.descriptions:
            self.load_data()

        # Assign the descriptions to the addon based on the id
        if 0 <= self.id < len(Addon.titles) and 0 <= self.id < len(Addon.descriptions):
            self.title = Addon.titles[self.id]
            self.description = Addon.descriptions[self.id]
        else:
            self.title = "Addon"
            self.description = "This is an addon"

    @classmethod
    def load_data(cls):
        """
        Load the titles and descriptions from the files.
        """
        title_path = "Feast_txts/Addons_Titles.txt"
        description_path = "Feast_txts/Addons_Descriptions.txt"

        try:
            # Load the titles and descriptions from the files
            with open(title_path, 'r') as file:
                cls.titles = [title.strip() for title in file.read().split('* ') if title.strip()]
            
            with open(description_path, 'r') as file:
                cls.descriptions = [desc.strip() for desc in file.read().split('* ') if desc.strip()]
        except FileNotFoundError:
            print("Error: Could not load addon data.")
            cls.titles = ["Addon"]
            cls.descriptions = ["This is an addon"]
        except Exception as e:
            print(f"Error: {e}")
            cls.titles = ["Addon"]
            cls.descriptions = ["This is an addon"]

    @classmethod
    def get_all_addons(cls,num_addons: int = 9) -> list:
        """
        Return a list of all addons.

        Parameters
        ----------
        list
            the list of all addons
        """
        addons = []
        for i in range(1, num_addons + 1):
            addon = cls(i)
            addons.append(addon)
        return addons 

    def __str__(self):
        return f"{self.title}: {self.description}"
    
    def __repr__(self):
        return f"<Addon id={self.id}, title='{self.title}', description='{self.description}'>"

if __name__ == "__main__":
    all_addons = Addon.get_all_addons()
    for addon in all_addons:
        print()
        print(addon)