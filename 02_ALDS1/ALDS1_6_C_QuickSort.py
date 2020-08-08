def partition(a, p, r):
    """パーティション分割"""
    x = int(a[r].split()[1])
    i = p - 1
    for j in range(p, r):
        if int(a[j].split()[1]) <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


def quick_sort(a, p, r):
    if p < r:
        # パーティション分割し、基準値を取得
        q = partition(a, p, r)

        # 基準値を境目に更にパーティション分割を実施
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)


n = int(input())
li = [input().splitlines()[0] for x in range(n)]
stable = sorted(li, key=lambda x: int(x.split()[1]))
# print(f"{li=}")
# print(f"{stable=}")

quick_sort(li, 0, n - 1)
# print(f"{li=}")
print("S" if stable == li else "Not s", end="")
print("table")
for i in li:
    print(i)
