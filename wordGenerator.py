import string
import random


def createScrabbleDistribution():
    # A-9, B-2, C-2, D-4, E-12, F-2, G-3, H-2, I-9, J-1, K-1, L-4, M-2, N-6, O-8,
    # P-2, Q-1, R-6, S-4, T-6, U-4, V-2, W-2, X-1, Y-2, Z-1 and Blanks-2.
    scrabbleSet = ""
    scrabbleSet += "aaaaaaaaa"
    scrabbleSet += "bb"
    scrabbleSet += "cc"
    scrabbleSet += "dddd"
    scrabbleSet += "eeeeeeeeeeee"
    scrabbleSet += "ff"
    scrabbleSet += "ggg"
    scrabbleSet += "hh"
    scrabbleSet += "iiiiiiiii"
    scrabbleSet += "j"
    scrabbleSet += "k"
    scrabbleSet += "llll"
    scrabbleSet += "mm"
    scrabbleSet += "nnnnnn"
    scrabbleSet += "oooooooo"
    scrabbleSet += "pp"
    scrabbleSet += "q"
    scrabbleSet += "rrrrrr"
    scrabbleSet += "ssss"
    scrabbleSet += "tttttt"
    scrabbleSet += "uuuu"
    scrabbleSet += "vv"
    scrabbleSet += "ww"
    scrabbleSet += "x"
    scrabbleSet += "yy"
    scrabbleSet += "z"
    return scrabbleSet

class WordGenerator:
    def __init__(self):
        self.scrabbleDistribution = createScrabbleDistribution()

    def generateRandomWord(self, wordLength):
        generatedWord = ""
        for x in range(0, wordLength):
            generatedWord += random.choice(self.scrabbleDistribution)
        return generatedWord





