# Imports
import translators as ts
import os
import pinyin
from tqdm import tqdm

# Opening the file
os.chdir("word-list")
all_text_file_chinese = open("all-chinese.txt", "r")
all_text_file_english = open("all-english.txt", "w")
all_text_file_pinyin = open("all-pinyin.txt", "w")

all_text_pinyin = ""
all_text_english = ""
all_text_chinese_list = all_text_file_chinese.readlines()

# Translating each line
for word in tqdm(all_text_chinese_list):
    
    word = word.replace("\n", "") # Stripping newline character
    # Adding to the english string
    # all_text_english += ts.google(word, from_language='zh', to_language='en')
    all_text_english += "\n"

    # Adding to the pinyin string
    all_text_pinyin += pinyin.get(word)
    all_text_pinyin += "\n"
    #print(f"Chinese:{word}, Pinyin:{pinyin.get(word)}")

# Writing the files
all_text_file_english.write(all_text_english)
all_text_file_pinyin.write(all_text_pinyin)

# Closing the files
all_text_file_chinese.close()
all_text_file_english.close()
all_text_file_pinyin.close()