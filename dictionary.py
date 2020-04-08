import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print( "Did you mean %s instead." % get_close_matches(w, data.keys())[0])
        a= input( "Please Enter 'Y' or 'N'.: ")
        if a == 'Y':
            return word
        else:
            pass
    else:
        print("Word entered by You is wrong. Please re-check it.")

word = input("Enter word: ")

print(translate(word))

