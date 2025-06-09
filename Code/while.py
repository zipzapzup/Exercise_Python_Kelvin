# C:\Python36
# Testing of while statement  - control flow
# while Statements is a looping statement and can have an optional else clause

number = 33
running = True

while running:
    guess = int(input('Enter an integer:'))

    if guess == number:
        print('Congratulations, you guess it right')
        # This change the state of the while loop to stops
        running = False
    elif guess < number:
        print('No, the number is a little higher')
    else:
        print('No, the number is a little lower')
else:
    print('The while loop is over')
    # Do anything you want here

print('Done')
