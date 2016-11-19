#!/usr/bin/env python3
# define a function to load the dictionary to internal structure
# we will load it from external file
def load_dict(path):
    in_file = open(path, 'r')
    arrayOfWords = []
    for line in in_file:
        arrayOfWords.append(line.rstrip("\n"))
    in_file.close()
    return arrayOfWords

#a = load_dict("C:\Atom\Python\Hackaton\PythonHackaton\words.txt")
a = ["lots", "hackaton", "loto"]

#enteredWord = input("Provide the word to find anagrams for: ")
enteredWord = "slot"
b = []
for word in a:
    if len(word) == len(enteredWord):
        b.append(word)

c = []
for words in b:
    print(words)


print(c)



# process the input word we're working with

# logic behind the anagram program
# ideal case - work with the internal structure (array) with all
# words from the dictionary and try to find proper letters in those words
# it is up to you how you'll handle this area, try to figure this out

# print the requested anagrams
