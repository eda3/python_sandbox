li = [[[0] * 10 for i in range(3)] for j in range(4)]

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())

    for j in range(len(li)):
        for k in range(len(li[j])):
            for m in range(len(li[j][k])):
                if j == b-1 and k == f-1 and m == r-1:
                    li[b-1][f-1][r-1] += v

for i in range(len(li)):
    for f in li[i]:
        for r in f:
            print(" {}".format(r), end="")
        print("")
    if i != len(li)-1:
        print("#" * 20)
