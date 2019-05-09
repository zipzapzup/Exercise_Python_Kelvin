# C:\Python36
# Testing of while statement using my own login

supermarket = True
inventory = []
count = 0
while supermarket and count < 3:
    print("\n prologue - walking*** \n \n You are walking in a supermarket")
    print("As you walk through the aisle, you are thinking")
    print("What do you want to buy?")
    decision = str(input("There is a chicken and a beef: "))
    if decision == "chicken":
        print(" \n \n prologue - you have taken something*** \n \n You have taken a chicken!! :)")
        inventory.append("chicken")
        count = count + 1
    elif decision == "beef":
        print(" \n \n prologue - you have taken something*** \n \n You have taken a beef!! :|")
        inventory.append("beef")
        count = count + 1
    else:
        print("THere is only a chicken and a beef, other words mean that you didn't take anything")
        print("\n You wasted time **** \n")
        print("You go one more round")
        count = count + 1
else:
    print("You went home.")
    print("You found that you have \n \n ***In your plastic bag*** \n")
    for i in inventory:
        print(i)
    print("\n \n End")
