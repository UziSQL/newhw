def sum_of_squares(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i ** 2

    return total

print(sum_of_squares(5)) # 55