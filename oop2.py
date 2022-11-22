class Boxer:
    def __init__(self, size, strength, wins, losses):
        self.size = size
        self.strength = strength
        self.wins = wins
        self.losses = losses


def takeBet():
    boxer1 = Boxer(1, 1, 0, 1)
    boxer2 = Boxer(2, 2, 1, 0)

    userInput = input("Please choose a boxer. Enter 1 or 2.\n")

    winner = "boxer2"
    if (boxer1.size + boxer1.strength > boxer2.size + boxer2.strength):
        winner = "boxer1"

    if ((userInput == "1" and winner == "boxer1") or (userInput == "2" and winner == "boxer2")):
        print("You win the bet!")

    else:
        print("You lose. Loser.")


takeBet()
