# Code to solve N people in a circle puzzle (Josephus problem)
# See https://en.wikipedia.org/wiki/Josephus_problem

N = 5
K = 2

active = K  # which person will be removed next
people = list(range(N))

while len(people) > 1:
    print(people)
    print("removing", people[active])
    people = people[:active] + people[active+1:]
    active = (active + K - 1) % len(people)
    print()

print("The answer is:", people[0])
