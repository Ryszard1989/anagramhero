from wordChecker import *
import time
from wordGenerator import *
import csv
from csv import reader
import pickle

def getHighScoresFromFile(fp):
    # read csv file as a list of lists
    with open(fp, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
    loadedScores = []
    for row in list_of_rows[1:]:
        loadedScores.append(row)
    return loadedScores

class GameManager:
    def __init__(self):
        self.highScoreFP = "anagramHeroHighScores.csv"
        self.highScoreTable = getHighScoresFromFile(self.highScoreFP) #Load from file
        self.currentScore = 0 #Reset for each user in a given session
        self.highSessionScore = 0
        self.wordChecker = WordChecker()
        self.wordGenerator = WordGenerator()
        self.gameLength = 10
        self.userEnteredWord = ""
        self.generatedWord = ""
        self.start = time.time()
        self.currentTime = time.time()

    def manageGame(self):
        self.printHighScores()
        self.kickOffNewGame()
        while self.currentTime - self.start < self.gameLength:
            print("")
            self.showUserNewGeneratedWord()
            self.takeUsersEnteredWord()
            wordScore = self.calculateWordScore()
            self.updateCurrentScore(wordScore)
            self.updateCurrentTime()
        self.endGame()
        self.recordHighScore()
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

    def recordHighScore(self):
        # take second element for sort
        def takeSecond(elem):
            return int(elem[1])
        self.highScoreTable.sort(key=takeSecond, reverse=True)
        newHighScore = False
        for score in self.highScoreTable:
            if self.currentScore > int(score[1]) or len(self.highScoreTable)<5:
                newHighScore = True
                print("You got a new high score!")
                userName = raw_input("Enter your name: ")
                highScore = [userName, self.currentScore]
                break
        if newHighScore is True:
            self.highScoreTable.append(highScore)
        self.highScoreTable.sort(key=takeSecond, reverse=True)
        self.printHighScores()
        with open(self.highScoreFP, 'wb') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(['name', 'score'])
            for x in range(5):
                csv_out.writerow(self.highScoreTable[x])

    def printHighScores(self):
        dash = '-' * 20
        print(dash)
        print("{:^20s}".format("HIGH SCORES"))
        print(dash)
        #for num, score in enumerate(self.highScoreTable, start=1):
            #print("{}: {} - {}".format(num, score[0], score[1]))
        for num, score in enumerate(self.highScoreTable, start=1):
            print("{:<1}: {:<9s} - {:>3}".format(num, score[0], score[1]))
        print(dash)

    def offerReplay(self):
        playAgain = raw_input("Play again? y/n")
        if playAgain is 'y':
            self.currentScore = 0
            self.manageGame()