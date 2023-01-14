import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def translate(word):
    try:
        word = word.lower().strip()
        if word in data:
            return data[word]
        elif word.title in data:
            return data[word.title()]
        elif len(get_close_matches(word, data.keys())) > 0:
            new_word = get_close_matches(word, data.keys())[0]
            print(new_word)
            yn = input(
                f"Did you mean '{new_word}'? Enter [Y] if Yes or [N] if No: ")

            if yn == "Y":
                return data[new_word]
            elif yn == "N":
                return "Word does not exist."
            else:
                return "We didn't understand your entry."
        else:
            return "Word does not exist."
    except Exception as e:
        print(e)


print(translate(input("Enter word: ")))
