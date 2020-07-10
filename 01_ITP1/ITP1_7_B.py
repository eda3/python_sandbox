import itertools as it

n, x = map(int, input().split())

while True:
    if n == 0 and x == 0:
        break

    res = 0
    li = range(1, n + 1, 1)
    for c in it.combinations(li, 3):
        res += 1 if sum(c) == x else 0
    print(res)

    n, x = map(int, input().split())
