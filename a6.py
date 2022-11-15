import random


def rollDice():
    print()
    print("-----------------------------------------------------")
    print("Time to roll some dice!")

    chosen = -1
    badInput = True
    while (badInput):
        print("Pick a number on a D6 (1-6, inclusive)")

        userInput = input()
        print()

        try:
            # Enforce the conversion to an integer because python is a foul heathen language.
            chosen = int(userInput)

        # Defensive programming in case y'all wanna break my code.
        except ValueError:
            print("Why would you try to break the program? Do it right.")
            print()
            continue

        # Player makes an invalid choice
        if chosen < 1 or chosen > 6:
            print(
                "You know that you need to pick a number between 1 and 6, inclusive. Do it again.")
            print()
            continue

        else:
            badInput = False

    roll = -1
    rollCount = 0
    while (chosen != roll):
        roll = random.randint(1, 7)
        rollCount += 1

    print("You have successfully rolled", chosen)
    print("It took", rollCount, "rolls")
    print()
    print("Thanks for playing!")
    print("-------------------------------------------------------------")
    print()


rollDice()
