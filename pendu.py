import data

import functions
from random import randrange

score = functions.retreiveScore(data.saveFile)
print(score)

#get a random word, split it in list, create another list with letters replaced with "_" and get number of letters to find.
randWord = data.words[randrange(10)]
randWordSplit = list(randWord)
randWordToGuess = list("_"*len(randWordSplit))
letterToGuess = len(randWordSplit)

tries = 0
givenLetters=[]

pseudo = input("Whats your name ? ")

while letterToGuess > 0:
    print("".join(randWordToGuess))
    guessedLetter = functions.inputLetter(givenLetters)
    tries+=1
    givenLetters.append(guessedLetter)
    if guessedLetter in randWordSplit:
        letterFound = [randWordSplit.index(letter,i) for i,letter in enumerate(randWordSplit) if letter is guessedLetter]
        print("yeah you found {} letter".format(len(letterFound)))
        letterToGuess-=len(letterFound)
        functions.fillWordToGuess(letterFound,randWordToGuess,guessedLetter)
    else:
        print("This letter isn't in the word to guess")

score[pseudo]=tries
functions.saveScore(score,data.saveFile)
