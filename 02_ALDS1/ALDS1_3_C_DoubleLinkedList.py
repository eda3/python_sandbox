from collections import deque

n = int(input())
d = deque()
for i in range(n):
    x = input().split()

    if x[0] == "insert":
        d.appendleft(x[1])
    elif x[0] == "delete":
        if x[1] in d:
            d.remove(x[1])
    elif x[0] == "deleteFirst":
        d.popleft()
    elif x[0] == "deleteLast":
        d.pop()

print(*d)
