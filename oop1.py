class Car:
    def __init__(self, topSpeed):
        self.topSpeed = topSpeed
        self.location = 0

    def printTopSpeed(self):
        print("Your top speed is:", self.topSpeed)

    def drive(self):
        self.location = self.location + 10

    def stop(self):
        print("Your final location is:", self.location)


def doCarStuff():
    myCar = Car(10)

    myCar.printTopSpeed()

    myCar.drive()
    myCar.drive()

    myCar.stop()


doCarStuff()
