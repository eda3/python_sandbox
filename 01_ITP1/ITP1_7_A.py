m, f, r = map(int, input().split())

while True:
    if m == -1 and f == -1 and r == -1:
        break

    res = m + f
    if m == -1 or f == -1:
        print("F")
    elif 80 <= res:
        print("A")
    elif 65 <= res:
        print("B")
    elif 50 <= res:
        print("C")
    elif 30 <= res:
        if 50 <= r:
            print("C")
        else:
            print("D")
    else:
        print("F")

    m, f, r = map(int, input().split())
