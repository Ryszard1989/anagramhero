from wordChecker import *
import time
from wordGenerator import *
from highScore import *
from scoreCalculator import *

class GameManager:
    def __init__(self):
        self.highScoreFP = "anagramHeroHighScores.csv"
        self.highScoreTable = HighScoreTable(self.highScoreFP)
        self.currentScore = 0 #Reset for each user in a given session
        self.wordChecker = WordChecker()
        self.wordGenerator = WordGenerator()
        self.gameLength = 60
        self.userEnteredWord = ""
        self.generatedTiles = ""
        self.start = time.time()
        self.currentTime = time.time()

    def manageGame(self):
        self.highScoreTable.printHighScores()
        self.kickOffNewGame()
        while self.currentTime - self.start < self.gameLength:
            print("")
            self.showUserNewGeneratedTiles()
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

    def showUserNewGeneratedTiles(self):
        self.generatedTiles = self.wordGenerator.generateRandomWord(7)
        print("Make a word from: ")
        print(self.generatedTiles.tiles)
        if self.generatedTiles.multiplier:
            if self.generatedTiles.doubleLetter:
                self.printLetterBonus(2)
            elif self.generatedTiles.tripleLetter:
                self.printLetterBonus(3)
            elif self.generatedTiles.doubleWord:
                print("*DOUBLE WORD SCORE*")
            elif self.generatedTiles.tripleWord:
                print("*TRIPLE WORD SCORE*")

    def printLetterBonus(self, bonusMultiplier):
        if bonusMultiplier is 2:
            letterIndex = self.generatedTiles.tiles.find(self.generatedTiles.doubleLetter)
        elif bonusMultiplier is 3:
            letterIndex = self.generatedTiles.tiles.find(self.generatedTiles.tripleLetter)
        multiplierIndicator = ""
        for i in range(len(self.generatedTiles.tiles)):
            if i is letterIndex:
                multiplierIndicator += '^'
            else:
                multiplierIndicator += ' '
        multiplierDetail = [' '] * 8
        multiplierDetail[letterIndex] = 'x'
        multiplierDetail[letterIndex + 1] = str(bonusMultiplier)
        print(multiplierIndicator)
        print(''.join(multiplierDetail))

    def takeUsersEnteredWord(self):
        self.userEnteredWord = raw_input("Enter word: ")

    def calculateWordScore(self):
        validWord = self.wordChecker.checkWord(self.userEnteredWord, self.generatedTiles.tiles)
        wordValue = 0
        if validWord:
            wordValue = scoreCalculator(self.userEnteredWord, self.generatedTiles)
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
