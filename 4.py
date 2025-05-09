def count_vowels(s: str) -> int:
    vowels = "aeiou"
    count = 0
    for i in s.lower():
        if i in vowels:
            count += 1
    return count

print(count_vowels('hello')) # 2