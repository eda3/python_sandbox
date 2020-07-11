x, y, z = map(int, input().split())

A = []
for _ in range(x):
    A.append([int(x) for x in list(input().split())])

B = []
for _ in range(y):
    B.append([int(x) for x in list(input().split())])


C = [[0] * z for _ in range(x)]

for k in range(z):
    for i in range(x):
        for j in range(y):
            C[i][k] += A[i][j] * B[j][k]

for i in range(len(C)):
    for j in range(len(C[i])):
        if j != len(C[i]) - 1:
            print("{} ".format(C[i][j]), end="")
        else:
            print(C[i][j])

