n = int(input())
(*li,) = map(int, input().split())
input()
(*Q,) = map(int, input().split())

bits = 1
for i in li:
    # print(f"{i=}")
    # print(f"{bin(bits)=}")
    bits |= bits << i
    # print(f"{bin(bits)=}")
    # print()

# print()
for q in Q:
    # print(f"{bin(bits)=}")
    print("yes" * ((bits >> q) & 1) or "no")
    # print()
