x, y, z = map(int, input().split())
a = 0
count = 0
for i in range(x):
    n = int(input())
    if i + 1 == x or z <= n:
        a += n * count
        count = 0
    elif n <= y:
        a -= n
        count += 1
print(a)
