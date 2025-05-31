def wordPattern(pattern: str, s: str) -> bool:
    s_list = s.split(" ")

    # Check if pattern length matches the number of words
    if len(pattern) != len(s_list):
        return False

    # Create mapping dictionary
    mapping = {
        key: value for key, value in zip(pattern, s_list)
    }

    # Check if the mapping is one-to-one
    if len(set(mapping.values())) != len(mapping.values()):
        return False

    # Create the result string
    result = ""
    for char in pattern:
        result += mapping[char]

    # Final check if the result matches the original string
    return result == s.replace(" ", "")

pattern = "aaaa"
s = "dog cat cat fish"

result = wordPattern(pattern, s)
print(result)
