from Addon import title, description 
from Guest import title, description 
from Table import title, description 

        
        
class Loader:
    """
    Loads both titles and descriptions

    Attributes
    ----------
    title_addons : list
        the titles of the addons
    title_guests : list
        the titles of the guests
    title_tables : list
        the titles of the tables

    desc_addons : list
        the descriptions of the addons
    desc_guests : list
        the descriptions of the guests
    desc_tables : list
        the descriptions of the tables
    """
    
    # The titles and descriptions for the addons, guests, and tables
    title_addons = []
    title_guests = []
    title_tables = []

    # Load the titles and descriptions from the files
    desc_addons = []
    desc_guests = []
    desc_tables = []

def  __init__(self, id: int) -> None:
    # Load the titles and descriptions if not already loaded
    if not Loader.title_addons or not Loader.title_guests or not Loader.title_tables:
        # Load ids for the addons, guests, and tables
        self.assign_description(id, "addon")
        self.assign_description(id, "guest")
        self.assign_description(id, "table")
        
        self.load_data()

@classmethod
def assign_description(self, id, item_type):
    if item_type == "addon":
        if 0 <= id < len(Loader.title_addons) and 0 <= id < len(Loader.desc_addons):
            self.title = Loader.title_addons[id]
            self.description = Loader.desc_addons[id]
        else:
            self.title = "Addon"
            self.description = "This is an addon"
    
    elif item_type == "guest":
        if 0 <= id < len(Loader.title_guests) and 0 <= id < len(Loader.desc_guests):
            self.title = Loader.title_guests[id]
            self.description = Loader.desc_guests[id]
        else:
            self.title = "Guest"
            self.description = "This is a guest"
    
    elif item_type == "table":
        if 0 <= id < len(Loader.title_tables) and 0 <= id < len(Loader.desc_tables):
            self.title = Loader.title_tables[id]
            self.description = Loader.desc_tables[id]
        else:
            self.title = "Table"
            self.description = "This is a food item"
    else:
        self.title = "Unknown"
        self.description = "This is an unknown item type"

@classmethod
def load_data(cls):
    """
    Load the titles and descriptions from the files.
    """
    title_addon_path = "Feast_txts/Addons_Titles.txt"
    desc_addon_path = "Feast_txts/Addons_Descriptions.txt"
    title_guest_path = "Feast_txts/Guests_Titles.txt"
    desc_guest_path = "Feast_txts/Guests_Descriptions.txt"
    title_table_path = "Feast_txts/Tables_Titles.txt"
    desc_table_path = "Feast_txts/Tables_Descriptions.txt"

    try:
        # Load the titles and descriptions from the files
        with open(title_addon_path, 'r') as file:
            cls.title_addons = [title.strip() for title in file.read().split('* ') if title.strip()]
        
        with open(desc_addon_path, 'r') as file:
            cls.desc_addons = [desc.strip() for desc in file.read().split('* ') if desc.strip()]
        
        with open(title_guest_path, 'r') as file:
            cls.title_guests = [title.strip() for title in file.read().split('* ') if title.strip()]
        
        with open(desc_guest_path, 'r') as file:
            cls.desc_guests = [desc.strip() for desc in file.read().split('* ') if desc.strip()]
        
        with open(title_table_path, 'r') as file:
            cls.title_tables = [title.strip() for title in file.read().split('* ') if title.strip()]
        
        with open(desc_table_path, 'r') as file:
            cls.desc_tables = [desc.strip() for desc in file.read().split('* ') if desc.strip()]
    except FileNotFoundError:
        print("Error: Could not load data.")
        cls.title_addons = ["Addon"]
        cls.desc_addons = ["This is an addon"]
        cls.title_guests = ["Guest"]
        cls.desc_guests = ["This is a guest"]
        cls.title_tables = ["Table"]
        cls.desc_tables = ["This is a food item"]
    except Exception as e:
        print(f"Error: {e}")
        cls.title_addons = ["Addon"]
        cls.desc_addons = ["This is an addon"]
        cls.title_guests = ["Guest"]
        cls.desc_guests = ["This is a guest"]
        cls.title_tables = ["Table"]
        cls.desc_tables = ["This is a food item"]

def assigment(self):
    """ 
    Assign data to the appropriate class
    """
    
    # Assign the descriptions to the addon based on the id
    if 0 <= self.id < len(Loader.title_addons) and 0 <= self.id < len(Loader.desc_addons):
        self.Addon.title = Loader.title_addons[self.id]
        self.Addon.description = Loader.desc_addons[self.id]
    else:
        self.Addon.title = "Addon"
        self.Addon.description = "This is an addon"

    # Assign the descriptions to the guest based on the id
    if 0 <= self.id < len(Loader.title_guests) and 0 <= self.id < len(Loader.desc_guests):
        self.Guest.title = Loader.title_guests[self.id]
        self.Guest.description = Loader.desc_guests[self.id]
    else:
        self.Guest.title = "Guest"
        self.Guest.description = "This is a guest"

    # Assign the descriptions to the table based on the id
    if 0 <= self.id < len(Loader.title_tables) and 0 <= self.id < len(Loader.desc_tables):
        self.Table.title = Loader.title_tables[self.id]
        self.Table.description = Loader.desc_tables[self.id]
    else:
        self.Table.title = "Table"
        self.Table.description = "This is a food item"


if __name__ == "__main__":
    # Create an instance of the Loader class
    loader = Loader()

    # Assign data to the appropriate class
    loader.assigment()

    # Access the title attribute from the Guest class
    print(Guest.title)
    for title, desc in zip(Guest.title, Guest.description):
        print(f"Title: {title}, Description: {desc}")