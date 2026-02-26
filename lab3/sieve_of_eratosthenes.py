# Sieve of Eratosthenes implementation
# See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

N = 272
# False => number is prime
# True => number is composite
a = [False] * N
for i in range(2, N):
    if not a[i]:
        print(i, end=" ")
        for j in range(i+i, N, i):
            a[j] = True
