from collections import deque

d = deque()
li = list(input().split())
for i in li:
    if i in "+-*":
        b = d.pop()
        a = d.pop()
        d.append(str(eval(a + i + b)))
    else:
        d.append(i)

print(str(d[0]))
