from typing import List


def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [2,2,1,1,1,2,2]

result = majorityElement(nums)
print(result)