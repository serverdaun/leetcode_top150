from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    i = 0
    while i <= (min([len(x) for x in strs]) - 1):
        for elem in strs[1:]:
            if elem[i] != prefix[i]:
                return prefix[:i]
        i += 1
    return prefix[:i]

# strs = ["flower", "flow", "flght"]
strs = ["dog", "rececar", "car"]
# strs = ["flow", "flower", "flo"]


result = longestCommonPrefix(strs=strs)
print(result)
