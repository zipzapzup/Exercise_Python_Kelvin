alice = input().split()
bob = input().split()

# Compare Triplets Challenge
# 2 Input of 3 entries, where each numerator needs to be compared.
# If Alice's input is less than Bob's input. Alice scores 1 point
# If Alice's input is equal to Bob. No one scores.
# If Alice's input is greater than Bob, Bob wins.

def compareTriplet(list1, list2):
    alicewin = 0
    bobwin = 0
    for i in range (len(list1)):
        if (list1[i] < list2[i]):
            alicewin += 1
        elif (list1[i] == list2[i]):
            continue
        elif (list1[i] > list2[i]):
            bobwin += 1
    print(str(alicewin) + ' ' + str(bobwin))


compareTriplet(alice, bob)
