def isIsomorfict(s: str, t: str) -> bool:
    mapping = {
        key: value for key, value in zip(s, t)
    }
    
    if len(set(mapping.values())) != len(mapping.values()):
        return False

    result = ""
    for char in s:
        result += mapping[char]

    return result == t


s = "badc"
t = "baba"


result = isIsomorfict(s, t)
print(result)