import csv
from csv import reader
import os.path

def getHighScoresFromFile(fp):
    # read csv file as a list of lists
    fileExists = os.path.exists(fp)
    print(fileExists)
    if fileExists:
        openMode = 'r'
    else:
        openMode = 'w+'
    with open(fp, openMode) as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
    loadedScores = []
    for row in list_of_rows[1:]:
        loadedScores.append(row)
    return loadedScores


class HighScoreTable:
    def __init__(self, fp='default.csv'):
        self.fp = fp
        self.highScoreTable = getHighScoresFromFile(self.fp)  # Load from file

    def recordHighScore(self, currentScore):
        # take second element for sort
        def takeSecond(elem):
            return int(elem[1])
        self.highScoreTable.sort(key=takeSecond, reverse=True)
        newHighScore = False
        def userInputHighScore(aHighScore):
            print("You got a new high score!")
            userName = raw_input("Enter your name: ")
            scoreDetails = [userName, aHighScore]
            return scoreDetails
        if len(self.highScoreTable) == 0:
            newHighScore = True
            highScore = userInputHighScore(currentScore)
        else:
            for score in self.highScoreTable:
                if currentScore > int(score[1]) or len(self.highScoreTable)<5:
                    newHighScore = True
                    highScore = userInputHighScore(currentScore)
                    break
        if newHighScore:
            self.highScoreTable.append(highScore)
        self.highScoreTable.sort(key=takeSecond, reverse=True)
        del self.highScoreTable[5:] #TODO - potential bug here when high score is last on list?
        with open(self.fp, 'wb') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(['name', 'score'])
            for x in range(len(self.highScoreTable)):
                csv_out.writerow(self.highScoreTable[x])
            out.close()



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

