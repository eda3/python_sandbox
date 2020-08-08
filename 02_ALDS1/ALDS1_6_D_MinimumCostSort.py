n = int(input())
li = [int(x) for x in list(input().split())]
sorted_list = sorted(li)
si = sorted_list[:]
cost = 0
for i in range(n):
    print(f"{i=}")
    print(f"{sorted_list[i]=}")
    print(f"{li.index(sorted_list[i])=}")
    # ソート済みリストからインデックス取得
    a_idx = li.index(sorted_list[i])
    j = 0
    while i < a_idx:
        j += 1
        print(f" {li=}")
        print(f" {si=}")
        print(f" {j=}")
        print(f" {a_idx=}")
        print(f" {sorted_list[a_idx]=}")
        print(f" {li.index(sorted_list[a_idx])=}")
        b_idx = li.index(sorted_list[a_idx])
        print(f" {cost=}")
        cost += li[b_idx]
        print(f" {cost=}")
        li[a_idx], li[b_idx] = li[b_idx], li[a_idx]
        a_idx = b_idx
        print()

    print(f"{sorted_list[i]=}")
    print(f"{sorted_list[0]=}")
    print(f"{sorted_list[i]*j=}")
    print(f"{sorted_list[i] * 2 + sorted_list[0] * (j + 2)=}")
    cost += sorted_list[i] * j
    print()
print(cost)

