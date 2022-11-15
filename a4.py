import random


def generateNum(lowerBound, upperBound):
    return random.randint(lowerBound, upperBound+1)


def main():
    guessNum = generateNum(1, 10)

    currGuess = -1
    while (currGuess != guessNum):
        print("Guess an integer from 1 to 10, inclusive.")

        userInput = input()

        try:
            currGuess = int(userInput)

        except ValueError:
            print("Why would you try to break the program? Do it right.")
            continue

        if currGuess > guessNum:
            print("Your number is too big.")

        elif currGuess < guessNum:
            print("Your number is too small")

        else:
            print("Correct!")


main()
