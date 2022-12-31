user_phrase = str(input("Say something: "))
paragraph = []


def sentence_maker(phrase):
    interrogatives = ("who", "what", "where", "when", "how")
    stripped_capitalized_phrase = phrase.capitalize().strip()
    
    if phrase.startswith(interrogatives):
        return f"{stripped_capitalized_phrase}?"
    
    return f"{stripped_capitalized_phrase}."


while user_phrase != "\end":
    paragraph.append(sentence_maker(user_phrase))
    user_phrase = str(input("Say something: "))

print(" ".join(paragraph))
