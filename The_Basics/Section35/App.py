import json
from difflib import SequenceMatcher
data = json.load(open("data.json"))

def translate(word):
    word = word.lower().strip()
    return data[word] if word in data else "Word does not exist."

print(translate(input("Enter word:")))