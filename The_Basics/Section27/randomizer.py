import random

def random_line(filename):
    with open(f"quotes/{filename}", 'r', encoding='cp850') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

print(random_line("unloved.txt"))

# temp = "happy"
# x = "s" if temp == "sad" else "h" if temp == "happy" else "u"
# print(x)