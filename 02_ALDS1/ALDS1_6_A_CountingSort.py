n = int(input())
a = [int(x) for x in list(input().split())]
b = [0] * (n + 1)
c = [0] * 10001
k = max(a)

# C[i] に i の出現数を記録する
for i in a:
    c[i] += 1

# C[i] に i以下の数の出現数を記録する
for i in range(1, k + 1):
    c[i] = c[i] + c[i - 1]

for i in reversed(a):
    b[c[i]] = i
    c[i] -= 1

print(*b[1:])
