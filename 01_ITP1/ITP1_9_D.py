s = list(input().replace("\r", "").replace("\n", ""))
n = int(input())
for i in range(n):
    li = list(input().split())
    if li[0] == "print":
        a = int(li[1])
        b = int(li[2])
        print("".join(s[a:b+1]))
    elif li[0] == "replace":
        a = int(li[1])
        b = int(li[2])
        p = list(li[3])
        s[a:b+1] = p
    elif li[0] == "reverse":
        a = int(li[1])
        b = int(li[2])
        p = s[a:b+1]
        p.reverse()
        s[a:b+1] = p
