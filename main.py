"""
This is a simple python dictionary that accepts input from
the user and displays the meaning of the word entered by
the user. Enjoy it.....LOL
"""
import json
from difflib import get_close_matches  #This library helps you compare user input and find similarities to a word(and in my case my vocabs)

data = json.load(open("vocabs.json"))  # To load the json file into python. I loaded it because the
                                       # file isn't large else i will have treat it as a database.

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:         #If the user enter delhi, it will check for Delhi as well
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]      #To check for words like UK, USA
    elif len(get_close_matches(word, data.keys())) > 0:
        decision = input("Did you mean %s? Enter Y if yes, or N if no: " %get_close_matches(word, data.keys())[0]).upper()
        if decision == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "N":
            return "The word does not exit. Please enter a valid word."
        else:
            return "Not sure what you are looking for dude"
    else:
        return "The word does not exit, Please enter a valid word."

word = input("Please enter the word to search for the meaning: ").lower()

output = translate(word)

if type(output) == list:              #Presents the output in a list form.
    for i in output:
        print(i)
else:
    print(output)
