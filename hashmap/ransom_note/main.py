from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:

    magazine_counter = Counter(magazine)
    ransom_note_counter = Counter(ransomNote)

    is_subset = all(ransom_note_counter[val] <= magazine_counter[val] for val in ransom_note_counter)
    return is_subset

ransomNote = "abca"
magazine = "aab"

result = canConstruct(ransomNote, magazine)
print(result)


# def canConstruct(ransomNote: str, magazine: str) -> bool:
#     # Create a dictionary to store character counts
#     dictionary = {}
#     # Iterate through the magazine and count characters
#     for char in magazine:
#         if char not in dictionary:
#             dictionary[char] = 1
#         else:
#             dictionary[char] += 1
#     # Iterate through the ransom note and check character counts
#     for char in ransomNote:
#         if char in dictionary and dictionary[char] > 0:
#             dictionary[char] -= 1
#         else:
#             return False
#     return True