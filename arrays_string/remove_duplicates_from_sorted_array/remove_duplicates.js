function removeDuplicates(nums) {
    let j = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] != nums[i - 1]) {
            nums[j] = nums[i];
            j += 1;
        }
    }
    return j;
}

nums = [0,0,1,1,1,2,2,3,3,4];
console.log(removeDuplicates(nums));
