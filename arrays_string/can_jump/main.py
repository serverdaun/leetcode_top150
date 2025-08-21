def can_jump(nums: list) -> bool:
    furthest = 0
    for i in range(len(nums)):
        if i > furthest:
            return False
        
        furthest = max(furthest, i + nums[i])

        if furthest >= (len(nums) - 1):
            return True

    return False

nums = [2, 3, 1, 1, 4]

result = can_jump(nums)
print(result)