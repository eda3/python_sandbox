N, M = map(int, input().split())

str_list = [input() for _ in range(N)]

li = []
for i, input_list in enumerate(str_list, start=1):
    point, Absenteeism_count = input_list.split()
    absent = int(Absenteeism_count) * 5
    result = int(point) - int(absent)
    if int(M) <= abs(result):
        li.append(i)

for i in li:
    print(i)
