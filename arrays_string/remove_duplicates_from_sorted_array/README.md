# Remove Duplicates from Sorted Array

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements must remain unchanged. Return the number of unique elements (`k`).

You must modify the array `nums` directly, placing the first `k` elements as the unique elements. Elements beyond the first `k` are irrelevant and will not affect the result.

## Task Requirements

- Modify the input array `nums` in-place.
- Return the integer `k`, representing the count of unique elements.
- Ensure the first `k` elements of `nums` contain the unique elements in their original order.

## Example

### Example 1:

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation:
Your function should return k = 2, and the first two elements of nums are 1 and 2. Remaining elements are irrelevant.
```

### Example 2:

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation:
Your function should return k = 5, and the first five elements of nums are 0, 1, 2, 3, and 4. Remaining elements are irrelevant.
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Custom Judge

The solution will be tested with the following code snippet:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // Expected unique elements

int k = removeDuplicates(nums); // Your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

// Accepted if no assertions fail
```

Ensure your solution satisfies the above criteria.

