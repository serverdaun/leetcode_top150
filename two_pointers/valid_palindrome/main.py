import string

def isPalindrome(s: str) -> bool:
    s = s.lower().strip()
    s = s.replace(" ", "")
    s = s.translate(str.maketrans('','', string.punctuation))
    return s[::-1] == s



s = "race a car"

result = isPalindrome(s)
print(result)
