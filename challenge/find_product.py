


product = [2,4,1,0,20]

# O(n) space complexity
# O(n^2) time complexity
def find_product(num: list):
    result = [None] * len(num)
    ptr1 = 0

    while ptr1 < len(result):
        total = 1
        for i in range( len(result)):
            if i == ptr1:
                continue
            total *= num[i]
        result[ptr1] = total
        ptr1 += 1

    return result

def find_product_two(nums):
    left = 1
    product = []
    # First pass: Calculate products starting from left
    for values in nums:
        product.append(left)
        left = left * values
        
    # Second pass: Update the product list by calculating products from right to left
    right = 1
    for i in range(len(nums)-1, -1, -1):
        product[i] = product[i] * right
        right = right * nums[i]

    return product


def main():
    inputs = [
        [1,2,3,1,10,0,3,1],
        [8,1,2,9,7,10,0],
        [1,2,1,5,10,0,3,1]
    ]

    for i in range(len(inputs)):
        print(
            "inputs: ", inputs[i]
            )
        print(
            "results: ", 
            find_product(inputs[i]), 
            find_product_two(inputs[i]),
            end="\n",
            )


if __name__== "__main__":
    main()