# Remove Duplicates from Sorted Array II

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

**Constraints:**
- Do not allocate extra space for another array
- You must do this by modifying the input array in-place with O(1) extra memory

## Examples

### Example 1:
```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

### Example 2:
```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Solution Approach

### Two-Pointer Technique

The solution uses a two-pointer approach to efficiently remove duplicates while maintaining O(n) time complexity and O(1) space complexity:

1. **Initialize pointers**: 
   - `write` pointer starts at index 2 (since we can always keep the first 2 elements)
   - `read` pointer starts at index 2

2. **Iterate through the array**:
   - For each element at position `read`, check if it's different from the element 2 positions back from `write`
   - If different, copy the element to the `write` position and increment `write`
   - If same, skip it (don't copy)

3. **Return the length**: The `write` pointer indicates the length of the modified array

### Algorithm Logic

- Since the array is sorted, we only need to compare with the element 2 positions back
- If `nums[read] != nums[write - 2]`, it means the current element won't create more than 2 duplicates
- This ensures each unique element appears at most twice in the result

## Time and Space Complexity

- **Time Complexity**: O(n) - we traverse the array once
- **Space Complexity**: O(1) - we only use a constant amount of extra space

## Custom Judge

The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

## Implementation

The solution is implemented in `remove_duplicates_2.py` using Python with the two-pointer technique described above.
