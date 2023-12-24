import os
#print all names of txt 

folder_path = "/home/bubbline/CodePython/The-Feast/Skrypty/Descriptionss"  # Replace with the path to your folder

# Check if the folder exists
if os.path.exists(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Filter out text files
    text_files = [file for file in file_list if file.endswith(".txt")]

    # Print the names of text files
    if text_files:
        print("Text files in the 'Descriptions' folder:")
        for text_file in text_files:
            print(text_file)
    else:
        print("No text files found in the 'Descriptionss' folder.")
else:
    print(f"The folder '{folder_path}' does not exist.")
