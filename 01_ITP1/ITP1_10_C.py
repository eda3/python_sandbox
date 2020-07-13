import statistics
while True:
    n = int(input())
    if n == 0:
        break

    li = [int(x) for x in list(input().split())]
    stdev = statistics.pstdev(li)
    print(round(stdev, 8))
