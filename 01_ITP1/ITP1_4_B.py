a, op, b = input().split()
a = int(a)
b = int(b)

while op != "?":
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)

    a, op, b = input().split()
    a = int(a)
    b = int(b)
