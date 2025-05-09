def digit_count(n: int) -> int:
    return len(str(abs(n)))

print(digit_count(123)) # 3
print(digit_count(4567)) # 4