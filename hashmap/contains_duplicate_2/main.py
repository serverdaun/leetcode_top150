def containsNearbyDuplicate(nums: list, k: int) -> bool:
    index_map = {}

    for i, num in enumerate(nums):
        print(f"Index map is as follows: {index_map}")
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i

    return False

nums = [1, 2, 3, 1]
k = 3

result = containsNearbyDuplicate(nums, k)
print(result)
