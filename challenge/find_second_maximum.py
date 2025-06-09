import sys
nums = [2,1,4,5,6,10,9]

def compare(x: int, y: int) -> int:
    if x <  y:
        return x    
    return y
    

def find_second_maximum(nums: list):
    length = len(nums)
    first = None
    second = None

    match length:
        case 0:
            return
        case 1 | 2:
            return compare(nums[0], nums[1])
        case _:
            pass
    
    if nums[0] > nums[1]:
        first, second = nums[0], nums[1]
    else:
        first, second = nums[1], nums[0]
    
    for i in range(2, len(nums)):
        if nums[i] >= first:
            second = first
            first = nums[i]
        elif nums[i] >= second:
            second = nums[i]
        else:
            continue

    return second    




def main():
    inputs = [
        [2,1,4,5,6,10,9],
        [10,1,3,1,0,20,19],
        [1,3,41,5,10,9],
        [4,10,10,8,9]
    ]

    for i in range(len(inputs)):
        print("inputs : ", inputs[i])
        print(
            find_second_maximum(inputs[i]),
            end="\n"
        )

if __name__=="__main__":
    main()