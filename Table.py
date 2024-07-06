class Table:
    """ A class to represent a food item in the game.

    Attributes
    ----------
    id : int
        the id of the food
    type : str
        the type of food
    isPicked : bool
        whether the food is isPicked
    title : str
        the title of the food
    description : str
        the description of the food
    """

    # Default values for attributes
    type = "Table"
    isPicked = False

    # Class-level attributes to hold titles and descriptions
    titles = []
    descriptions = []

    def __init__(self, id: int) -> None:
        self.id = id

        # Load data if not already loaded   
        if not Table.titles or not Table.descriptions:
            self.load_data()

        # Assign the descriptions to the food based on the id
        if 0 <= self.id < len(Table.titles) and 0 <= self.id < len(Table.descriptions):
            self.title = Table.titles[self.id]
            self.description = Table.descriptions[self.id]
        else:
            self.title = "Table"
            self.description = "This is a food item"

    @classmethod
    def load_data(cls):
        """
        Load the titles and descriptions from the files.
        """
        title_path = "Feast_txts/Tables_Titles.txt"
        description_path = "Feast_txts/Tables_Descriptions.txt"

        try:
            # Load the titles and descriptions from the files
            with open(title_path, 'r') as file:
                cls.titles = [title.strip() for title in file.read().split('* ') if title.strip()]
            
            with open(description_path, 'r') as file:
                cls.descriptions = [desc.strip() for desc in file.read().split('* ') if desc.strip()]
        except FileNotFoundError:
            print("Error: Could not load food data.")
            cls.titles = ["Table"]
            cls.descriptions = ["This is a food item"]
        except Exception as e:
            print(f"Error: {e}")
            cls.titles = ["Table"]
            cls.descriptions = ["This is a food item"]

    @classmethod
    def get_all_food(cls,  num_tables: int = 3) -> list:
        """
        Return a list of all food items.
        
        Parameters
        ----------
        num_tables : int
            the number of food items to return

        Returns
        -------
        list
            a list of Table objects
        """
        foods = []
        for i in range(1, num_tables + 1):
            food = cls(i)
            foods.append(food)
        return foods

    def __str__(self):
        return f"title: {self.title}, description: {self.description}, isPicked: {self.isPicked}"
    def __repr__(self):
        return f"<Table id={self.id}, title='{self.title}', description='{self.description}', isPicked={self.isPicked}>"

if __name__ == "__main__":
    all_food = Table.get_all_food()
    for food in all_food:
        print()
        print(food)