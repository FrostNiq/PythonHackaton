#!/usr/bin/env python3
import random
# define a function for generating a random word
def chooseRandomWordFromFile(path):
  wordFromFile = ""
  in_file = open(path, 'r')
  arrayOfWords = []

  for line in in_file:
    arrayOfWords.append(line.rstrip("\n"))
  in_file.close()

  randomNumber = random.randrange(len(arrayOfWords))

  wordFromFile = arrayOfWords[randomNumber]
  return wordFromFile

word = chooseRandomWordFromFile("C:\Atom\Python\Hackaton\PythonHackaton\words.txt")
#print(word)

lengthOfChoosenWord = len(word)
currentState = []
for i in range(lengthOfChoosenWord):
  currentState.append("_")
unsuccesfulAttempts = 0
win = False
# main loop
while unsuccesfulAttempts < 6 and win == False:
  # print out current state of the game
  # for example - We're guessing the word: _ _ _ _ _ _ _ _ _ _
  print("We're guessing the word: " + " ".join(currentState))
  # let's get a letter from the user
  inputLetter = False
  while inputLetter != True :
    letter = input("Guess the letter: ")
    # make sure the letter is only one character
    if len(letter) != 1:
      print("You must enter only one character!")
      continue

    # print the letter to see if everything is ok by now
    print("You guessed", letter)
    inputLetter = True


  # determine if the letter is in the word
  if word.find(letter) == -1:
    print("Letter is not in word")
    unsuccesfulAttempts += 1
  else:
    print("Letter is in word")
    #currentState[word.index(letter)] = letter
    for i in range(0, len(word)):
      if letter == word[i] :
        currentState[i] = letter
        i += 1

  # check if the word is not guessed in its entirety
  if word == "".join(currentState):
    print("You have won")
    win = True

  if unsuccesfulAttempts == 6 :
    print("You have lost!")
