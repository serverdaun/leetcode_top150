const needle = "sad";
const haystack = "sadbutsad";

function strStr(haystack, needle) {
    return haystack.indexOf(needle);
}

console.log(strStr(haystack, needle));
