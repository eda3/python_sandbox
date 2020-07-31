def is_prime(q, k=50):
    q = abs(q)
    if q == 0:
        return False
    elif q == 2:
        return True
    return pow(2, q - 1, q) == 1


n = int(input())
result = 0
for i in range(n):
    x = int(input())
    if is_prime(x):
        result += 1

print(result)
