print("Welcome to treasure island!!!")
print("let's begin shall we?")
print("Your mission is to find the treasure")

choice1 = input('You are at the crossroad, where do you wanto to go?\nType"left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You arrived at the lake. There is an island, there is a island in the middle.\nDo you wan to "swim" or "wait".\n').lower()
    if choice2 == "swim":
        choice3 = input('You finally arrived at the island. There is a house with three doors. "Red", "Green" and "Blue".\nChoose one.\n').lower()
        if choice3 == "red":
            print("Game over. you just fell into a dark hole...")
        elif choice3 == "green":
            print("Congratulations,You win. You found the treasure worth $5 million.")
        else:
            print("Game over! You entered the room with fire...")
    else:
        print("Game over! You are attacked by wild beasts..")
else:
    print("Game over! You are attacked by the crocs...")


    
            
