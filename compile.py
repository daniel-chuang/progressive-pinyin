# Imports
from pprint import pprint
import os
import re

### Opening the text files ###
os.chdir("./word-list")
if os.path.exists("all-chinese.txt"):
    os.remove("all-chinese.txt")

# Function for reading a file
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return(f.read())

# Setting up an empty string for all of the files
all_text = str()

# Going through all of the files
for file in os.listdir():
    if file.endswith(".txt"):
        all_text = all_text + read_text_file(file)

# Filtering out numbered lines
all_text = re.sub("\/\/ \d*-\d*\n", "", all_text, 99999)

# Writing a new file with everything
all_text_file = open("all-chinese.txt", "w")
all_text_file.write(all_text)

all_text_file.close()
