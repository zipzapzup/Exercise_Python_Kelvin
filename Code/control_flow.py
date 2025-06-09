number = 33
guess = int(input('Enter an integer: '))

if guess == number:
    # New block in here
    print("Congratulations, you guessed it.")
    print("But you do not win any prizes!")
    # End of the new block
elif guess < number:
    # Another block
    print("No, the value is a little higher")
else:
    print("No, its a little lower than that")

print("Done")
# This last statement is always executed
# After the if statement is executed
