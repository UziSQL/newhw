def count_words(s: str) -> int:
    word = s.split()
    return len(word)

print(count_words('Hello World!')) # 2