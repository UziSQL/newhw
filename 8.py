def collatz_sequence_length(n: int) -> int:
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

print(collatz_sequence_length(788)) # 29