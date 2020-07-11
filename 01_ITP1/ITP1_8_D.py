s = input().replace("\r", "").replace("\n", "")
s *= 2
p = input().replace("\r", "").replace("\n", "")
print("Yes" if p in s else "No")
