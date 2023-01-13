import json
from difflib import get_close_matches
import random

class Dictionary:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.data = json.load(f)

    def lookup(self, word):
        word = word.lower().strip()
        if word in self.data:
            return self.data[word]
        elif len(get_close_matches(word, self.data.keys())) > 0:
            new_word, meaning = self.selectFromMultipleCloseMatches(word)
            meaning = self.selectFromMultipleMeaning(meaning)
            return f"{new_word}: {meaning}"
        else:
            return "Word not found."

    def selectFromMultipleCloseMatches(self, word):
        suggestion = get_close_matches(word, self.data.keys())
        user_choice = input(f"Did you mean {suggestion}? ")
        print(suggestion)
        while True:
            if user_choice in suggestion:
                return (user_choice, self.data[user_choice])
            else:
                self.selectFromMultipleCloseMatches(word)
    
    def selectFromMultipleMeaning(self, list_of_meanings):
        return random.choice(list_of_meanings) if len(list_of_meanings) > 0 else list_of_meanings[0]
        
d = Dictionary('data.json')
print(d.lookup('cour'))
