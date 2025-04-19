# My solution
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # print(f"i={nums[i]}, j={nums[j]}")
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimized solution
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap = {}
    #     for i in range(len(nums)):
    #         hashmap[nums[i]] = i
    #     for i in range(len(nums)):
    #         complement = target - nums[i]
    #         if complement in hashmap and hashmap[complement] != i:
    #             return [i, hashmap[complement]]
    #     # If no valid pair is found, return an empty list
    #     return []
