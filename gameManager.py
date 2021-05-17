
class GameManager:
    def __init__(self):
        self.HighScoreTable = {} #Load from file
        self.currentScore = 0 #Reset for each user in a given session
        self.possibleWords = [] #Load english dictionary from file


    def startGame(self):
        print("new game started")
