def print_alphabets():
    # Alphabets is represented in Unicode
    # Since there are 26 alphabets
    # We need to create 26 lists consisting of 0
    # A starts with Unicode 97
    alphabet = [0] * 26
    uni_code = 97
    # Fill in the alphabet
    for i in range(26):
        alphabet[i] = uni_code
        uni_code += 1
    print(alphabet)

    # Convert to alphabets
    for i in range(len(alphabet)):
        alphabet[i] = chr(alphabet[i])
    
    return alphabet
        

print(print_alphabets())