def numSum(startNum, endNum):
    sum = 0
    for i in range(startNum, endNum + 1):
        sum += i

    print("The sum is:", sum)


def fizzBuzz():
    for i in range(1, 101):
        if (i % 2 == 0):
            print("BUZZ")
        else:
            print("FIZZ")


def minMaxAverage(inList):
    print("Min:", min(inList))
    print("Max:", max(inList))
    print("Average:", sum(inList) / len(inList))


def main():
    inList = [1, 2, 3, 4, 5]

    numSum(1, 15)
    fizzBuzz()
    minMaxAverage(inList)


main()
