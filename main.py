from gameManager import *

def main():
    dash = '-' * 40
    print(dash)
    print("{:^40}".format("ANAGRAM HERO"))
    print(dash)
    gm = GameManager()
    gm.manageGame()

if __name__ == "__main__":
    main()