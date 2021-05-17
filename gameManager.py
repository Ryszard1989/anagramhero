from wordChecker import *
import string
import random

def generateRandomWord(wordLength):
    lowerLetters = string.ascii_lowercase
    generatedWord = ""
    for x in range(0, wordLength):
        generatedWord += random.choice(lowerLetters)
    return generatedWord

class GameManager:
    def __init__(self):
        self.HighScoreTable = {} #Load from file
        self.currentScore = 0 #Reset for each user in a given session
        self.wordChecker = WordChecker()

    def startGame(self):
        print("new game started")
        userEnteredWord = ""
        while userEnteredWord != "Quit":
            generatedWord = generateRandomWord(10)
            print("")
            print("Make a word from: " + generatedWord)
            userEnteredWord = raw_input("Enter word: ")
            wordValue = self.wordChecker.checkWord(userEnteredWord, generatedWord)
            print()
            print ("Word score: " + str(wordValue))
            self.currentScore += wordValue
            print ("Current Score: " + str(self.currentScore))
        print ("Final Score: " + str(self.currentScore))

