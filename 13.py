def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b

    return abs(a)

print(gcd(56, 98)) # 14
print(gcd(27, 15)) # 3