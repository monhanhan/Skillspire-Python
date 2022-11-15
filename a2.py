def printList():
    list = ["PeePee", "PooPoo", "Man", "Labs",
            "Are", "Not", "My", "Friend", "Homie", "Why"]

    for i in range(5, 10):
        print(list[i])

    # I assume that when you say "Between index 3 and 10" you mean all items from 3 to 10, exclusive, since there can't be an index 10.
    for i in range(4, 10):
        print(list[i])


def main():
    printList()


main()
