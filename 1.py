def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False

    return True

print(is_prime(2)) # False
print(is_prime(3)) # True