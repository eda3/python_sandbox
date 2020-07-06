from typing import List

input_line = int(input())
A = 0
B = 0
for i in range(int(input_line)):
    s: List[str] = input().rstrip().split(" ")
    if s[0].startswith("SET"):
        if s[1] == "1":
            A = int(s[2])
        if s[1] == "2":
            B = int(s[2])
    elif s[0].startswith("ADD"):
        B = A + int(s[1])
    elif s[0].startswith("SUB"):
        B = A - int(s[1])

print(A, B)
