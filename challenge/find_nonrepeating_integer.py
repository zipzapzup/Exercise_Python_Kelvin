
nums = [11,-11, 22, 33, -33, 11]

# O(n) time complexity
# O(n) space complexity
def find_first_nonrepeating(nums: list):
    counter = {}
    result = []
    for i in nums:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
        
    for i in range(len(nums)):
        if counter[nums[i]] == 1:
            result.append(nums[i])
    
    return result[0]



def main():
    inputs = [
        [11,-11, 22, 33, -33, 11],
        [8,-11, 8, -11, -33, 7],
        [7,1,2,2,7,9,8]
    ]

    for i in range(len(inputs)):
        print("inputs: ", inputs[i])
        print(
            "answers: ",
            find_first_nonrepeating(inputs[i]),
            end="\n"
        )

if __name__=="__main__":
    main()