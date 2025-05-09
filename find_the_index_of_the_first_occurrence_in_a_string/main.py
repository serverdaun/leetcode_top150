def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1


haystack="sadbutsad"
needle="sad"

result = strStr(haystack=haystack, needle=needle)
print(result)

