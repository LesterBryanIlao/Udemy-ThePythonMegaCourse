import json
from difflib import get_close_matches
import random


class Dictionary:
    def __init__(self, json_file):
        self.data = json.load(open(json_file))

    def lookup(self, word):
        word = word.lower().strip()
        if word in self.data:
            return self.stringFormat(word, self.selectFromMultipleMeaning(self.data[word]))
        elif len(get_close_matches(word, self.data.keys())) > 0:
            # new_word, meaning = self.selectFromMultipleCloseMatches(word)
            # meaning = self.selectFromMultipleMeaning(meaning)
            # return f"{new_word}: {meaning}"

            new_word = get_close_matches(word, self.data.keys())[0]
            return self.stringFormat(new_word, self.selectFromMultipleMeaning(self.data[new_word]))

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

    def stringFormat(self, word, meaning):
        return f"{self.clean(word)}: {meaning}"

    def clean(self, word):
        return word.strip().title()


d = Dictionary('data.json')
print(d.lookup('shit'))
