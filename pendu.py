import data

import functions
from random import randrange

#pseudo = input("Whats your name ? ")

randWord = data.words[randrange(10)]

randWordSplit = list(randWord)
randWordToGuess = "_"*len(randWordSplit)


print("debug:")
print(randWordSplit)
print("===")

print("")
print("here is the word to guess:")
print("".join(randWordToGuess))

guessLetter = input("give me a letter")

if guessLetter in randWordSplit:
    letterFound = [randWordSplit.index(letter,i) for i,letter in enumerate(randWordSplit) if letter is guessLetter]
    print("yeah you found {} letter".format(len(letterFound)))

else:
    print("This letter isn't in the word to guess")
