
# O(n logN) time complexity
# O(1) space - sort
def find_minimum_sort(nums: list):
    nums.sort()
    return nums[0]

# O(n) time complexity
# O(1) space complexity - linear search
def find_minimum(nums: list):
    if len(nums) == 0:
        return None
    
    minimum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < minimum:
            minimum = nums[i]
    
    return minimum



def main():
    inputs = [
        [10,12,8,10,3,19,30],
        [7,5,8,3,5,7,1],
        [19,17,40,11,10]
    ]

    for i in range(len(inputs)):
        print(
            "inputs :", inputs[i], 
            end="\n")
        print(
            "find_minimum : ",
            find_minimum(inputs[i])
        )


if __name__ == "__main__":
    main()