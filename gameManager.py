from wordChecker import *

class GameManager:
    def __init__(self):
        self.HighScoreTable = {} #Load from file
        self.currentScore = 0 #Reset for each user in a given session
        self.wordChecker = WordChecker()

    def startGame(self):
        print("new game started")
        userEnteredWord = ""
        while userEnteredWord != "Quit":
            userEnteredWord = raw_input("Enter word: ")
            wordValue = self.wordChecker.checkWord(userEnteredWord)
            print (wordValue)

    #def generateRandomWord(self, wordLength):
    #    for 1:wordLength:
