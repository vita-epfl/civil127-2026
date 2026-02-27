# Solution for lab 3.5 from
# https://github.com/vita-epfl/civil127-2026/blob/main/lab3/lab3.pdf

for code in range(0, 9999):
    s = str(code).zfill(4)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])

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
