import sys
import json

path = "data.json"

try:
    f = open(path, "r")
    contents= json.load(f) #this will be a dictionary
    print(contents)
    f.close()
except:
    contents= {}

key = input("Please enter a new key > ")
value = input("Please enter a new value > ")

#add it to the dictionary
contents[key] = value

#update the file
f= open(path, "w")
json.dump(contents, f)
f.close()
