input()
A = [int(x) for x in list(input().split())]
# 数列の最後の値を基準値にする
x = A[-1]
i = -1

r = len(A)
for j in range(r):
    print(f"{A=}")
    print(f"{i=}")
    print(f"{j=}")
    # print(f"{A[j]=}")
    # 各値がxより大きいか小さいかで振り分ける
    if A[j] <= x:
        i += 1
        # A[i]とA[j]を交換
        A[i], A[j] = A[j], A[i]
    print(f"{A=}")
    print()

# 基準値の前後に[ ]を追加
A[i] = "[" + str(A[i]) + "]"
print(*A)
