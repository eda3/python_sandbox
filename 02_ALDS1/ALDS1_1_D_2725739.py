import sys

max_value = 1e10
min_value = -max_value
input()
for v in map(int, sys.stdin):
    if min_value < v - max_value:
        min_value = v - max_value
    if v < max_value:
        max_value = v
print(min_value)
