input()
li1 = [int(x) for x in list(input().split())]
input()
li2 = [int(x) for x in list(input().split())]

counter = 0
for i in li2:
    if i in li1:
        counter += 1
print(counter)
