import sys


def insert_sort(A, n, g):
    global cnt

    # 指定値のgからリストの大きさまで繰り返す
    for i in range(g, n, 1):
        # print(f"bef{A=}")
        # 最初にヒットした数値
        v = A[i]
        j = i - g
        # print(f"{j=}")
        while 0 <= j and v < A[j]:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v
        # print(f"aft{A=}")


n = int(input())
A = [x for x in map(int, sys.stdin)]

cnt = 0
G = [1]
while n >= 3 * G[-1] + 1:
    G.append(3 * G[-1] + 1)


for g in G[::-1]:
    insert_sort(A, n, g)
print(len(G))
G.reverse()
print(*G)
print(cnt)
for a in A:
    print(a)
