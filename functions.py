import pickle
import os

def inputLetter(givenLetters):
    guessedLetter = input("input a letter:")
    if not guessedLetter.isalpha():
        print("give me a letter !")
        inputLetter(givenLetters)
    elif guessedLetter in givenLetters:
        print("you already gave that letter !")
        inputLetter(givenLetters)
    else:
        return guessedLetter

def fillWordToGuess(letterFound,randWordToGuess,guessedLetter):
    for i in letterFound:
        randWordToGuess.pop(i)
        randWordToGuess.insert(i,guessedLetter)

def saveScore(data, saveFile):
    with open(saveFile, "wb") as file:
        dataPickled = pickle.Pickler(file)
        dataPickled.dump(data)

def retreiveScore(saveFile):
    if not os.path.exists(saveFile):
        saveScore({},saveFile)
    with open(saveFile, "rb") as file:
        dataUnpickled = pickle.Unpickler(file)
        score = dataUnpickled.load()
        return score

