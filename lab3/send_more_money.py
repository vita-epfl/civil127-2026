# Bruteforce SEND+MORE=MONEY puzzle

for s in range(1, 10):  # we start at 1 for s
    for e in range(0, 10):
        for n in range(0, 10):
            for d in range(0, 10):
                for m in range(1, 10):  # we start at 1 for m
                    for o in range(0, 10):
                        for r in range(0, 10):
                            for y in range(0, 10):
                                # check that we have unique values by
                                # creating a set and checking its len
                                values = {s, e, n, d, m, o, r, y}
                                if len(values) == 8:
                                    send = 1000*s + 100*e + 10*n + d
                                    more = 1000*m + 100*o + 10*r + e
                                    money = 10000*m + 1000*o + 100*n + 10*e + y
                                    if send + more == money:
                                        print(send)
                                        print(more)
                                        print("=====")
                                        print(money)
