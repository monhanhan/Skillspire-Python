import random


class BigCat():
    def __init__(self):
        self.speed = 5
        self.strength = 5
        self.intelligence = 5
        self.health = 5
        self.durability = 5


class Lion(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 50
        self.health = 50

    def king(self, inCat):
        if (isinstance(inCat, Cheetah)):
            if (inCat.escape(self)):
                return

        inCat.speed = 0
        inCat.strength = 0
        inCat.intelligence = 0
        inCat.health = 0
        inCat.durability = 0


class Cheetah(BigCat):
    def __init__(self):
        super().__init__()
        self.speed = 75
        self.strength = 25
        self.intelligence = 25
        self.health = 25
        self.durability = 25

    def escape(self, inCat):
        randNum = random.randint(1, 11)
        if (randNum > 4):
            inCat.health = inCat.health - 20
            return True

        else:
            return False

    # I am going to assume that the run method hurts the other cat and not the cheetah. The instructions were unclear.
    def run(self, inCat):
        if (isinstance(inCat, Lion)):
            inCat.king(self)

        if (isinstance(inCat, Leopard)):
            inCat.attack(self)

        # This goes here so that cheetahs don't just live forever when they run into each other.
        else:
            self.escape(inCat)


class Leopard(BigCat):
    def __init__(self):
        super().__init__()
        self.strength = 30
        self.intelligence = 30
        self.health = 30

    def attack(self, inCat):
        if (isinstance(inCat, Lion)):
            inCat.king(self)
            return

        elif (isinstance(inCat, Cheetah)):
            if (inCat.escape(self)):
                return

        inCat.health = inCat.health - 15


def main():
    print()
    print("The battle begins!")
    bigBoi = Lion()
    fastBoi1 = Cheetah()
    fastBoi2 = Cheetah()
    fastBoi3 = Cheetah()
    spottyBoi1 = Leopard()
    spottyBoi2 = Leopard()

    catList = [bigBoi, fastBoi1, fastBoi2,
               fastBoi3, spottyBoi1, spottyBoi2]

    # While there are still cats in the list they will battle.
    while (len(catList) > 1):
        print(catList[0].__class__.__name__,
              "VS", catList[1].__class__.__name__)

        # If the first cat in the list is a lion we will call king()
        if (isinstance(catList[0], Lion)):
            catList[0].king(catList[1])

        # If the first cat is a cheetah we will call run()
        elif (isinstance(catList[0], Cheetah)):
            catList[0].run(catList[1])

        # If we get here it means that our cat is a leapard and we call attack()
        else:
            catList[0].attack(catList[1])

        if (catList[1].health < 1):
            print(catList[1].__class__.__name__, "Is defeated!")
            catList.pop(1)

        if (catList[0].health < 1):
            print(catList[0].__class__.__name__, "Is defeated!")
            catList.pop(0)

    print("The", catList[0].__class__.__name__, "Wins the battle!")


main()
