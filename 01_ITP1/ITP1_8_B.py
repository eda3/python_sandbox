while True:
    s = input()
    if s == "0":
        break
    li = list(s)
    sums = sum([int(x) for x in li])
    print(sums)
