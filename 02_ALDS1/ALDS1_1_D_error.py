from collections import deque


def recursive_diff_check(dq):
    max_value = -9999999999999999999999999999

    dq_len = len(dq)
    for i in range(dq_len):
        for j in range(i+1, dq_len, 1):
            # print(f"{j=}, {i=}")
            # print(f"{dq[i]=}, {dq[j]=}")
            tmp = dq[j] - dq[i]
            if max_value < tmp:
                max_value = tmp
            # print(f"{max_value=}")
            # print("")
    return max_value


n = int(input())
li = deque([int(input()) for _ in range(n)])
# li = []
# for i in range(n):
#     li.append(int(input()))

# すべて同じ値ならば0を返却
if len(set(li)) == 1:
    print(0)
else:
    # 最小値
    min_value = min(li)

    # 末尾と末尾-1が最小値ならば0を返却
    # 最小値のインデックス番号
    min_idx = li.index(min_value)
    print(recursive_diff_check(li))
