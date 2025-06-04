def isAnagram(s: str, t: str) -> bool:
    if len(t) < len(s):
        return False

    t_dict = {
        key: value for key, value in enumerate(t)
    }

    for _, v in t_dict.items():
        if v not in s:
            return False
        else:
            s = s.replace(v, "", 1)

    return True

s = "anagram"
t = "nagaram"

result = isAnagram(s, t)
print(result)

# Optimal solution
# from collections import Counter

# def isAnagram(s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)
