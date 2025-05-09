import math

def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

print(is_perfect_square(9)) # True
print(is_perfect_square(10)) # False