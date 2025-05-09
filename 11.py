def is_palindrome(s: str) -> bool:
    if s[::-1] == s:
        return True

    return False

print(is_palindrome('racecar')) # True
print(is_palindrome('Hello')) # False