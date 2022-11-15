import random


def rockPaperScissors():
    print()
    print("------------------------------------------------------------------------------")
    print("Let's Play Rock, Paper, Scissors!")

    # Set these values so that the while loop defaults to running without risking an error later.
    chosen, compHand = -1, -1
    while (chosen == compHand):
        # Generate a fresh throw every time we loop so that we aren't just going against one throw all the time.
        compHand = random.randint(1, 4)

        print("Choose your weapon")
        print("1=Rock, 2=Paper, 3=Scissors")

        userInput = input()
        print()

        try:
            # Enforce the conversion to an integer because python is a foul heathen language.
            chosen = int(userInput)

        # Defensive programming in case y'all wanna break my code.
        except ValueError:
            print("Why would you try to break the program? Do it right.")
            print()
            chosen = compHand
            continue

        if chosen == compHand:
            # This is a tie. The loop will run again.
            print("You threw the same as the computer. Try again!")
            print()

        # Player makes an invalid choice
        elif chosen < 1 or chosen > 3:
            # reset to tie conditions so that we loop again.
            chosen = compHand
            print("You know that you need to pick 1, 2, or 3. Do it again.")
            print()

        else:
            # Player chooses rock
            if chosen == 1:
                # computer chooses paper
                if compHand == 2:
                    print("Paper beats rock! You lose!")

                # computer chooses scissors
                else:
                    print("Rock beats Scissors! You win!")

            # Player chooses paper
            if chosen == 2:
                if compHand == 1:
                    print("Paper beats rock! You win!")

                else:
                    print("Scissors beats paper! You Lose!")

            # player chooses scissors
            if chosen == 3:
                if compHand == 1:
                    print("Rock beats Scissors! You lose!")

                else:
                    print("Scissors beats paper! You win!")

    print()
    print("Thanks for playing!")
    print("------------------------------------------------")
    print()


rockPaperScissors()
