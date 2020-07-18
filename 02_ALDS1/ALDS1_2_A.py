input()
A = [int(x) for x in list(input().split())]

flag = True
n = len(A)
counter = 0
while flag:
    flag = False
    for j in range(n-1, 0, -1):
        if A[j] < A[j-1]:
            tmp = A[j]
            A[j] = A[j-1]
            A[j-1] = tmp
            flag = True
            counter += 1

print(" ".join(str(x) for x in A))
print(counter)


