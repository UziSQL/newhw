def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(1999)) # False
print(is_leap_year(2000)) # True