const nums = [2, 2, 1, 1, 1, 2, 2,];

function majorityElement(nums) {
    let candidate = undefined;
    let majCount = 0;

    for (const elem of nums) {
        if (majCount === 0) {
            candidate = elem;
            majCount = 1
        } else if (candidate === elem) {
            majCount += 1;
        } else {
            majCount -= 1;
        }
    }
    
    return candidate;
}

console.log(majorityElement(nums))
