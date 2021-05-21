import csv
from csv import reader

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
        for score in self.highScoreTable:
            if currentScore > int(score[1]) or len(self.highScoreTable)<5:
                newHighScore = True
                print("You got a new high score!")
                userName = raw_input("Enter your name: ")
                highScore = [userName, currentScore]
                break
        if newHighScore is True:
            self.highScoreTable.append(highScore)
        self.highScoreTable.sort(key=takeSecond, reverse=True)
        self.printHighScores()
        with open(self.fp, 'wb') as out:
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

