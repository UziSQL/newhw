def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(8)) # True
print(is_power_of_two(10)) # False