def rotate(nums: list, k: int) -> list:
    n = len(nums)
    k = k % n # for cases with k > len(nums)

    nums.reverse()

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    

# nums = [-1, -100, 3, 99]
# k = 2

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

rotate(nums=nums, k=k)
print(nums)
