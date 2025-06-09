lista = [2,31,54,10,2]
listb = [10,2,10,30,10]

def merge_list(nums1: list, nums2: list):
    combined_list = nums1 + nums2
    i = 0

    while i < len(combined_list) - 1:
        ptrb = i + 1
        while ptrb < len(combined_list):
            if combined_list[i] > combined_list[ptrb]:
                combined_list[i], combined_list[ptrb] = combined_list[ptrb], combined_list[i]
            ptrb += 1
        i += 1
    return combined_list


# time complexity O(n+m)
# space complexity O(n+m)
def merge_list_3_pointers(nums1: list, nums2: list) -> list:
    new_list = [None] * (len(nums1) + len(nums2))
    p1 = 0
    p2 = 0
    p3 = 0

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            new_list[p3] = nums1[p1]
            p1 += 1
            p3 += 1
        else:
            new_list[p3] = nums2[p2]
            p2 += 1
            p3 += 1
        
    if p1 == len(nums1) and p2 == len(nums2):
        return new_list
    
    if p1 == len(nums1):
        new_list[p3:] = nums2[p2:]
    elif p2 == len(nums2):
        new_list[p3:] = nums1[p1:]
    
    return new_list


def main():
    inputs = [
        ([2,3,10,15,20], [1,2,30,31,32]),
        ([1,1,2,3,5], [2,2,3,4,5]),
    ]

    print("merge list:", end="\n")
    for i in range(len(inputs)):
        print(merge_list(
                inputs[i][0], 
                inputs[i][1]
            ))
    
    print("merge list three pointer:", end="\n")
    for i in range(len(inputs)):
        print(merge_list_3_pointers(
            inputs[i][0],
            inputs[i][1]
        ))


if __name__ == "__main__":
    main()