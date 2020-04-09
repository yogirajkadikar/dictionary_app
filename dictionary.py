import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(( "Did you mean %s instead? Please Enter 'Y' or 'N'.:" % get_close_matches(w, data.keys())[0]))
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "Please Double check your query."    
    else:
       return "Word entered by You is wrong. Please re-check it."

word = input("Enter word: ")

output= (translate(word))

if type(output) == list:
    for item in output:
        print(output)
else:
    print(output)
