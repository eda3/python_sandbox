import sys
import string
li = []
for l in sys.stdin:
    for ll in list(l.lower()):
        li.append(ll)

d = dict([(x, 0) for x in string.ascii_lowercase])

for i in li:
    if i in d:
        d[i] += 1

for i in d.items():
    print(i[0], ":", i[1])
