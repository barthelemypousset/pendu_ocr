import pickle

def saveScore(data, saveFile):
    with open(saveFile, "wb") as file:
        dataPickled = pickle.Pickler(file)
        dataPickled.dump(data)

def retreiveScore(saveFile):
    with open(saveFile, "rb") as file:
        dataUnpickled = pickle.Unpickler(file)
        score = dataUnpickled.load()
        return score

