W, H, x, y, r = map(int, input().split())
check1 = True if 0 + r <= x <= W - r else False
check2 = True if 0 + r <= y <= H - r else False
print("Yes" if check1 and check2 else "No")
