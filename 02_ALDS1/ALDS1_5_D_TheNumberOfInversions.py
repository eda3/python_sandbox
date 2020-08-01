n = int(input())
A = [int(x) for x in list(input().split())]
B = [[A[i], i + 1] for i in range(n)]
B.sort()
A = [j for i, j in B]
bit = [0] * (n + 2)
ans = 0
for i in range(n):
    ret = 0
    a = A[i]
    while 0 < a:
        ret += bit[a]
        a -= a & (-a)
    ans += i - ret
    a = A[i]
    while a <= n:
        bit[a] += 1
        a += a & (-a)
print(ans)
