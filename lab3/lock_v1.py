# Solution for lab 3.5 from
# https://github.com/vita-epfl/civil127-2026/blob/main/lab3/lab3.pdf

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                # check that all digits are different by
                # putting the digits in a set and checking the
                # len
                ok = len({a, b, c, d}) == 4

                # check that the sum is 29
                ok = ok and (a + b + c + d == 29)

                # check that code is divisible by 13
                code = 1000 * a + 100 * b + 10 * c + d
                ok = ok and ((code * code - 1) % 13 == 0)

                if ok:
                    print(code)
