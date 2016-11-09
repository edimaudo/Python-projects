import random
def main():
    intro()
    inputvalue = input("How many rolls? ")
    while inputvalue.lower() not in ["no","exit"]:
        if not isinstance(int(inputvalue),int):
            print ("Please enter an integer number")
            inputvalue = input("How many rolls? ")
            break
        else:
            rolldice(inputvalue)
            inputvalue = input("Try Again? ")
            if inputvalue.lower() == "yes":
                inputvalue = input("How many rolls? ")
                break
    print("Thank you for playing the dice game") 
    exit()
    

def intro():
    print ("This program simulated the rolling of a pair of dice")
    print ("Type exit or no to end the game")
    print ("Type Yes to try again")
    print ("You enter the number of times you want the computer to 'Roll' the dice")
    

def rolldice(inputvalue):

    count = 0
    diceroll = []
    while count < inputvalue + 1:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice = dice1 + dice2
        diceroll.append(dice)
        count+=1
    print("Total spots   "+ "Number of rolls")
    print("  2            " + str(diceroll.count(2)))
    print("  3            " + str(diceroll.count(3)))
    print("  4            " + str(diceroll.count(4)))
    print("  5            " + str(diceroll.count(5)))
    print("  6            " + str(diceroll.count(6)))
    print("  7            " + str(diceroll.count(7)))
    print("  8            " + str(diceroll.count(8)))
    print("  9            " + str(diceroll.count(9)))
    print("  10           " + str(diceroll.count(10)))
    print("  11           " + str(diceroll.count(11)))
    print("  12           " + str(diceroll.count(12)))
        


if __name__ == "__main__":
    main()

#print (rolldice(1000))    
