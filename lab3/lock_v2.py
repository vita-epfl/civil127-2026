# Solution for lab 3.5 from
# https://github.com/vita-epfl/civil127-2026/blob/main/lab3/lab3.pdf

for code in range(0, 9999):
    a = code // 1000  # // is integer division
    b = (code // 100) % 10
    c = (code // 10) % 10
    d = code % 10

    # check that all digits are different by
    # putting the digits in a set and checking the
    # len
    ok = len({a, b, c, d}) == 4

    # check that the sum is 29
    ok = ok and (a + b + c + d == 29)

    # check that code is divisible by 13
    ok = ok and ((code * code - 1) % 13 == 0)

    if ok:
        print(code)
