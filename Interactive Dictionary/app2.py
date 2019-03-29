import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

def translate(w):
    if w.lower() in data:
        return data[w]
    elif w.capitalize() in data: # o método title() também funciona
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? \n Enter Y (yes) / N (no):" % get_close_matches(w, data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist, try another one"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist, try another one"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
