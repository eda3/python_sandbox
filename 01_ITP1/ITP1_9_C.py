n = int(input())
t = 0
h = 0
for i in range(n):
    li = [x for x in list(input().split())]
    if li[0] < li[1]:
        h += 3
    elif li[0] > li[1]:
        t += 3
    else:
        h += 1
        t += 1
print(t, h)
