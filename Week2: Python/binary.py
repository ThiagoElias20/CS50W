def binary(x):
    remainder = ""
    while x > 0:
        remainder = str(x % 2) + remainder
        x = x // 2
    return remainder