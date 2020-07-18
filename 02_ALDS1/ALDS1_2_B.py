input()
A = [int(x) for x in list(input().split())]
n = len(A)
counter = 0

for i in range(0, n-1, 1):
    minj = i
    for j in range(i, n, 1):
        if A[j] < A[minj]:
            minj = j
    if i == minj:
        continue
    tmp = A[i]
    A[i] = A[minj]
    A[minj] = tmp
    counter += 1

print(*A)
print(counter)
