W = input().replace("\r", "").replace("\n", "")
strings = []
while True:
    s = input().replace("\r", "").replace("\n", "")
    if s == "END_OF_TEXT":
        break

    for i in list(s.lower().split()):
        strings.append(i)

print(strings.count(W))
