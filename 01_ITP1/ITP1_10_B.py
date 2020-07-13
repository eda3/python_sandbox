import math
a, b, C = map(float, input().split())
cc = math.sin(math.radians(C))
S = 0.5 * a * b * cc
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C)))
H = S * 2 / a
print(S)
print(L)
print(H)
