n, m = map(int, input().split())
A = []
for i in range(n):
    A.append([int(x) for x in list(input().split())])

b = []
for i in range(m):
    result = 0
    b.append(int(input()))

for i in range(n):
    res = 0
    for bb, aa in zip(b, A[i]):
        res += bb * aa
    print(res)
