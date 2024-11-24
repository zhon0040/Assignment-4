import random
#Michael Zhong


def getCard():
    """
    Function returns card
    """
    return random.randint(1, 10)


#Main code
print("This program is basic blackjack but aces don't exist. Dealer stands on 17.\n")

while True:
    dealerNums = []
    dealerNums.append(getCard())
    dealerNums.append(getCard())
    print("The dealer has: ? " + str(dealerNums[1]))

    userNums = []
    userNums.append(getCard())
    userNums.append(getCard())
    print("You have: " + str(userNums[0]) + " " + str(userNums[1]) + " (" + str(sum(userNums)) + ")\n")

    while True:
        decision = input("Do you hit (H) or stand (S)?\n")
        if decision == "S" or decision == "s":
            print("Stand\n")

            print("You have ", end="")
            for i in userNums:
                print(str(i) + " ", end="")
            print("(" + str(sum(userNums)) + ")")

            while True:
                if sum(dealerNums) < 17:
                    dealerNums.append(getCard())
                else:
                    break

            print("The dealer had ", end="")
            for i in dealerNums:
                print(str(i) + " ", end="")
            print("(" + str(sum(dealerNums)) + ")\n")

            if sum(userNums) > sum(dealerNums):
                print("You win!\n")
                break
            else:
                print("You lose :(\n")
                break

        elif decision == "H" or decision == "h":
            print("Hit\n")
            userNums.append(getCard())

            print("You have ", end="")
            for i in userNums:
                print(str(i) + " ", end="")
            print("(" + str(sum(userNums)) + ")\n")

            if sum(userNums) > 21:
                print("Bust!")
                print("The dealer had ", end="")
                for i in dealerNums:
                    print(str(i) + " ", end="")
                print("(" + str(sum(dealerNums)) + ")\n")
                break

        else:
            print("That isn't an option. Try again.\n")

    while True:
        stop = input("Do you want to play again? (Y/N)\n")
        if stop == "N" or stop == "n":
            print("No\n")
            print("Goodbye")
            quit()
        elif stop == "Y" or stop == "y":
            print("Yes\n")
            break
        else:
            print("That isn't a valid input. Try again.\n")