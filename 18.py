def sum_of_cubes(n: int) -> int:
    return sum(i ** 3 for i in range(1, n + 1))

print(sum_of_cubes(3)) # 36
print(sum_of_cubes(4)) # 100