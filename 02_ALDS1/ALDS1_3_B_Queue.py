from collections import deque

n, q_time = map(int, input().split())
d = deque()
for i in range(n):
    x, y = input().split()
    d.append((x, int(y)))

total = 0
while d:
    name, time = d.popleft()
    if time <= q_time:
        total += time
        print(name, total)
    else:
        total += q_time
        time -= q_time
        d.append((name, time))
