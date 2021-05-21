from wordChecker import *
import time
from wordGenerator import *
from highScore import *

class GameManager:
    def __init__(self):
        self.highScoreFP = "anagramHeroHighScores.csv"
        self.highScoreTable = HighScoreTable(self.highScoreFP)
        self.currentScore = 0 #Reset for each user in a given session
        self.wordChecker = WordChecker()
        self.wordGenerator = WordGenerator()
        self.gameLength = 10
        self.userEnteredWord = ""
        self.generatedWord = ""
        self.start = time.time()
        self.currentTime = time.time()

    def manageGame(self):
        self.highScoreTable.printHighScores()
        self.kickOffNewGame()
        while self.currentTime - self.start < self.gameLength:
            print("")
            self.showUserNewGeneratedWord()
            self.takeUsersEnteredWord()
            wordScore = self.calculateWordScore()
            self.updateCurrentScore(wordScore)
            self.updateCurrentTime()
        self.endGame()
        self.highScoreTable.recordHighScore(self.currentScore)
        self.offerReplay()

    def kickOffNewGame(self):
        print("Make words of 2 or more letters from the letters provided.")
        raw_input("Hit any key to start your 60 seconds!")
        print("new game started")
        self.start = time.time()
        self.currentTime = time.time()

    def showUserNewGeneratedWord(self):
        self.generatedWord = self.wordGenerator.generateRandomWord(7)
        print("Make a word from: " + self.generatedWord)

    def takeUsersEnteredWord(self):
        self.userEnteredWord = raw_input("Enter word: ")

    def calculateWordScore(self):
        wordValue = self.wordChecker.checkWord(self.userEnteredWord, self.generatedWord)
        print ("Word score: " + str(wordValue))
        return wordValue

    def updateCurrentScore(self, wordScore):
        self.currentScore += wordScore
        print ("Current Score: " + str(self.currentScore))

    def updateCurrentTime(self):
        self.currentTime = time.time()
        print("Time left: " + str(self.gameLength - (self.currentTime - self.start)))

    def endGame(self):
        print("TIMES UP")
        print ("Final Score: " + str(self.currentScore))

    def offerReplay(self):
        playAgain = raw_input("Play again? y/n")
        if playAgain is 'y':
            self.currentScore = 0
            self.manageGame()