class Guests:
    def __init__(self,id: int):
        self.id = id
        self.name = name
        self.selected = selected
        self.title = title
        self.description = description
       
        load_descriptions()
  
    def load_descriptions(self):
        title_path1 = "Guests_Titles.txt"  # char title
      
        file_path  = "Guests Descriptions.txt"  # char description
        
        # Read the descriptions of the file
        with open(title_path1, 'r') as file:
            title = file.read()
      
        with open(file_path, 'r') as file:
            descriptions = file.read()
        
         
        # Split the descriptions into individual descriptions
        titles1 = title.split('* ')
      
        descriptions = descriptions.split('* ')
         
        titles1 = [title.strip() for title in titles1 if title.strip()]
        
        descriptions = [desc.strip() for desc in descriptions if desc.strip()]

        while i < 12:
            self.id = i+1
            self.title = titles1[i]
            self.description = descriptions[i]
            print(Guests.title)
            i += 1