n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    if a == "insert":
        d[b] = True
    elif a == "find":
        print("yes" if b in d.keys() else "no")
