import math
n = int(input())
a = [float(x) for x in list(input().split())]
b = [float(x) for x in list(input().split())]

result = 0
for aa, bb in zip(a, b):
    result += abs(aa - bb)
print(round(result, 6))

result = 0
for aa, bb in zip(a, b):
    result += abs(aa - bb) ** 2
print(round(math.sqrt(result), 8))

result = 0
for aa, bb in zip(a, b):
    result += abs(aa - bb) ** 3
print(round(math.pow(result, 1/3), 8))

result = []
for aa, bb in zip(a, b):
    result.append(abs(aa - bb))
print(max(result))
