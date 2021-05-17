import json

class WordChecker:
    def __init__(self):
        with open('words_dictionary.json') as json_file:
            self.possibleWords = json.load(json_file)

    def checkWord(self, proposedWord):
        if self.isValidWord(proposedWord):
            return(len(proposedWord))
        return 0

    def isValidWord(self,proposedWord):
        return proposedWord in self.possibleWords
