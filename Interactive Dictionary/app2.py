import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? \n Enter Y (yes) / N (no):" % get_close_matches(w, data.keys())[0])
        if yn = "Y":
            return data[dataget_close_matches(w, data.keys())[0]]
    else:
        return "The word doesn't exist, try another one"

word = input("Enter word: ")
print(translate(word))
