def lenghtOfLastWord(s: str) -> int:
    s_stripped = s.strip()
    last_word = s_stripped.split()[-1]
    return len(last_word)


s = "   fly me   to   the moon  "
result = lenghtOfLastWord(s)
print(result)
