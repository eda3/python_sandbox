while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    print(f"{x} {y}" if y > x else f"{y} {x}")
