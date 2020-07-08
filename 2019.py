import sympy

n = int(input())
str_list = [int(input()) for _ in range(n)]

for i in str_list:
    sums = sum(sympy.divisors(i)[:-1])
    if sums == i:
        print("perfect")
    elif abs(sums - i) == 1:
        print("nearly")
    else:
        print("neither")
