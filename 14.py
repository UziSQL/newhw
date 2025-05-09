def lcm(a: int, b: int) -> int:
    multiple = max(a, b)

    while not (multiple % a == 0 and multiple % b == 0):
        multiple += 1

    return multiple

print(lcm(5, 7)) # 35
print(lcm(6, 8)) # 24