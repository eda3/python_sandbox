x, y, z = map(int, input().split())
cnt = 0
for i in range(x, y + 1, 1):
    cnt += 1 if z % i == 0 else 0
print(cnt)
