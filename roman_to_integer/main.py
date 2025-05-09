def romanToInt(s: str) -> int:

    rules = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    sub_rules = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] + s[i+1] in sub_rules:
            result += sub_rules[s[i] + s[i+1]]
            i += 2
        else:
            result += rules[s[i]]
            i += 1

    return result


s = "MCMXCIV"

result = romanToInt(s)
print(result)
