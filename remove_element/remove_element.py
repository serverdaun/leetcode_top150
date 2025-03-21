from typing import List


def removeElement(nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)



nums = [3,2,2,3]
val = 3

output = removeElement(nums, val)
print(nums)
print(output)
