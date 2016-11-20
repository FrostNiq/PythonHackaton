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

arrayOfImportedWords = load_dict("C:\Atom\Python\Hackaton\PythonHackaton\words.txt")

enteredWord = input("Provide the word to find anagrams for: ")
#enteredWord = "Lots"
enteredWord = enteredWord.lower()
arrayOfWordsWithSameLength = []
for importedWord in arrayOfImportedWords:
    if len(importedWord) == len(enteredWord):
        arrayOfWordsWithSameLength.append(importedWord)

arrayOfAnagrams = []
for words in arrayOfWordsWithSameLength:
    result = True
    if sorted(enteredWord) == sorted(words) :
        arrayOfAnagrams.append(words)

print(arrayOfAnagrams)



# process the input word we're working with

# logic behind the anagram program
# ideal case - work with the internal structure (array) with all
# words from the dictionary and try to find proper letters in those words
# it is up to you how you'll handle this area, try to figure this out

# print the requested anagrams
