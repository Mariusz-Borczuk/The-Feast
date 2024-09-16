import os

id: int = 0
name: str = ""
selected: bool = False
title: str = ""
description: str = ""
status: str = ""
location: str = ""

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
 
titles1 = [titl.strip() for titl in titles1 if titl.strip()]
print(len(titles1))
descriptions = [desc.strip() for desc in descriptions if desc.strip()]
print(len(descriptions))
i = 0
while i < 12:
    id = i+1
    title = titles1[i]
    description = descriptions[i]
    print(title + " " + description)
    i += 1