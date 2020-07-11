while True:
    s = input().replace("\r", "").replace("\n", "")
    if s == "-":
        break
    n = int(input())
    for i in range(n):
        j = int(input())
        s = s[j:] + s[:j]
    print(s)
