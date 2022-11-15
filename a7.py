def takeInput():
    chosen = -1
    badInput = True
    while (badInput):
        print("Enter a positive integer")

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
        if chosen < 0:
            print(
                "You know that you need to pick positive integer. Do it again.")
            print()
            continue

        else:
            badInput = False

    return chosen


def getPercent(numPackages):
    if numPackages > 99:
        return .5

    elif numPackages > 49:
        return .4

    elif numPackages > 19:
        return .3

    elif numPackages > 10:
        return .2

    else:
        return 0


def main():
    print()
    print("----------------------------------------")
    print("Time to buy some software!")
    print("How many software packages do you want?")

    numPackages = takeInput()

    discountPercent = getPercent(numPackages)

    totalBeforeDiscount = numPackages * 99
    discount = totalBeforeDiscount * discountPercent

    total = round(totalBeforeDiscount - discount, 2)

    print("Your total is:", total)


main()
