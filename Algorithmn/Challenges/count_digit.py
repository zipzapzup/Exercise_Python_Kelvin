# Count Digits
from typing import List

def count_digit(nums: int) -> int:
    count = 0
    while nums > 0:
        nums = nums // 10
        count += 1
    return count
print(count_digit(4420))