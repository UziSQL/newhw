def factorial(n: int) -> int:
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

    return factorial

print(factorial(5)) # 120