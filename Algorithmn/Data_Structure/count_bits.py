# Count Bits

# Count number of bits that are set to 1
# 
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1 # add 1
        x >>= 1 # bitshift to the right
        
    return num_bits


def count_bits_my(x: int) -> int:
    bin_num = bin(x).lstrip('0b') # O(n) and O(n x m)
    count = 0 
    for i in bin_num:
        if i == '1':
            count += 1
        else:
            continue
    return count

print(count_bits(28))
print(count_bits_my(28))