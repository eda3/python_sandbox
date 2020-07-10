r, c = map(int, input().split())

res = [0 for i in range(c)]
for i in range(r):
    li = [int(x) for x in list(input().split())]
    for j, k in enumerate(li):
        print("{} ".format(k), end="")
        res[j] += k
    print(sum(li), end="")
    print("")

for rr in res:
    print("{} ".format(rr), end="")
print(sum(res))

