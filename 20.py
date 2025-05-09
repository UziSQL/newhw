def is_armstrong_number(n: int) -> bool:
    digits = str(n)
    num_digits = len(digits)

    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

    return sum_of_powers == n

print(is_armstrong_number(153)) # True
print(is_armstrong_number(370)) # True