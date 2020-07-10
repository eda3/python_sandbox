n = int(input())
flg = True
count = 0
while count < n:
    flg = True
    count += 1
    x = count
    if x % 3 == 0:
        print(" {}".format(count), end="")
        continue
    while x != 0 and flg:
        if x % 10 == 3:
            print(" {}".format(count), end="")
            flg = False
        x = x // 10
print("")
