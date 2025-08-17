def remove_duplicates(nums):
    """
    Remove duplicates in-place such that each unique element appears at most twice.
    Returns the length of the modified array.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(nums) <= 2:
        return len(nums)
    
    # Use two pointers: write pointer and read pointer
    write = 2  # Start from index 2 since we can always keep first 2 elements
    
    # Start reading from index 2
    for read in range(2, len(nums)):
        # If current element is different from the element 2 positions back,
        # it means we can include it (it won't create more than 2 duplicates)
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    
    return write

nums = [0,0,1,1,1,1,2,3,3]
print(remove_duplicates(nums))
