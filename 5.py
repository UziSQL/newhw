def sum_of_digits(n: int) -> int:
    digit = str(abs(n))

    total = 0
    for digit in digit:
        total += int(digit)

    return total

print(sum_of_digits(789)) # 24