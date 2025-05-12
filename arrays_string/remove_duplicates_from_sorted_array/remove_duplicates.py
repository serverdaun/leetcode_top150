from typing import List


# My solution
def removeDuplicates(nums: List[int]) -> int:
    for elem in nums:

        while nums.count(elem) > 1:
            nums.remove(elem)

    return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]

result = removeDuplicates(nums)
print(f"Len is {result}\nNums is: {nums}")


# Optimal solution
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
