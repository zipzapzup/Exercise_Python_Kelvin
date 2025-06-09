

# O(N *log(n))
def find_sum(nums: list, k: int):
    ptra = 0
    ptrb = len(nums) - 1
    nums.sort() 

    while ptra < ptrb:
        sum = nums[ptra] + nums[ptrb]
        if sum == k:
            return [
                nums[ptra], 
                nums[ptrb]
                ]
        elif sum < k:
            ptra += 1
        else:
            ptrb -= 1



def main():
    inputs = [
        [1,7,10,13,18,31,91],
        [9,10,30,10,40,99],
        [1,2,3,4,5,6,7,8]

    ]
    key = [
        17,
        39,
        13
    ]

    for i in range(len(inputs)):
        print("inputs is: ", inputs[i], "and target is :", key[i])
        print("find_sum() : ", find_sum(inputs[i], key[i]), end="\n\n")


if __name__== "__main__":
    main()