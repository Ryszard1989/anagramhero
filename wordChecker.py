import json

def isValidAnagram(proposedWord, generatedWord):
    sortedProposedWord = sorted(proposedWord)
    sortedGeneratedWord = sorted(generatedWord)
    # using issubset() to
    # check subset of list
    flag = 0
    if set(sortedProposedWord).issubset(set(sortedGeneratedWord)):
        flag = 1
    # printing result
    if (flag):
        print (proposedWord + " is valid anagram")
        return True
    else:
        print (proposedWord + " is not a valid anagram")
        return False

class WordChecker:
    def __init__(self):
        with open('words_dictionary.json') as json_file:
            self.possibleWords = json.load(json_file)

    def checkWord(self, proposedWord, generatedWord):
        if isValidAnagram(proposedWord, generatedWord):
            if self.isValidWord(proposedWord):
                return len(proposedWord)
            print(proposedWord + " is not a valid english word!")
        return 0

    def isValidWord(self,proposedWord):
        return proposedWord in self.possibleWords
