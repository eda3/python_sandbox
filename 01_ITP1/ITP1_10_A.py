import math
x1, y1, x2, y2 = map(float, input().split())
x = abs(x1 - x2)
y = abs(y1 - y2)
xx = x ** 2
yy = y ** 2
zz = xx + yy
z = math.sqrt(zz)
print(round(z, 8))
