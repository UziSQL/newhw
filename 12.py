def sum_of_multiples(n: int, x: int, y: int) -> int:
    total = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            total += i
    return total

print(sum_of_multiples(10, 3, 5)) # 33
print(sum_of_multiples(20, 7, 11)) # 32