d = {a:[] for a in range(1, 12)}
a = ""

with open("input.txt", "r", encoding='utf-8') as input:
    for line in input:
        line = line.split()
        d[int(line[0])] += [int(line[2])]

print(d)
for key in d:
    if len(d[key]) != 0:
        print(key,sum(d[key]) / len(d[key]))
    else:
        print(key,'-')
