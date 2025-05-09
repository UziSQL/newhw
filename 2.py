def nth_fibonacci(n: int) -> int:
    if n <= 0:
        return 0

    a, b = 1, 1
    for i in range(n - 2):
        a, b = b, a + b

    return b if n > 1 else 1

print(nth_fibonacci(4)) # 3