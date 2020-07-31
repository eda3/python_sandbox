import math


def kock(n, p1_x, p1_y, p2_x, p2_y):
    if n == 0:
        print(f"{p1_x:.8f} {p1_y:.8f}")
        return

    # p1, p2からs, t, uを計算

    # 与えられた線分(p1, p2) を3等分点s、tを求める
    s_x = (2 * p1_x + 1 * p2_x) / 3
    s_y = (2 * p1_y + 1 * p2_y) / 3

    t_x = (p1_x + 2 * p2_x) / 3
    t_y = (p1_y + 2 * p2_y) / 3

    # 線分を3等分する2点 s,t を頂点とする正三角形 (s,u,t) を作成する
    u_x = (
        (t_x - s_x) * math.cos(math.pi / 3) - (t_y - s_y) * math.sin(math.pi / 3) + s_x
    )
    u_y = (
        (t_x - s_x) * math.sin(math.pi / 3) + (t_y - s_y) * math.cos(math.pi / 3) + s_y
    )

    # 線分 (p1,s)、線分 (s,u)、線分 (u,t)、線分 (t,p2)に対して再帰的に同じ操作を繰り返す
    kock(n - 1, p1_x, p1_y, s_x, s_y)
    kock(n - 1, s_x, s_y, u_x, u_y)
    kock(n - 1, u_x, u_y, t_x, t_y)
    kock(n - 1, t_x, t_y, p2_x, p2_y)


n = int(input())
kock(n, 0, 0, 100, 0)
print("100.00000000 0.00000000")
