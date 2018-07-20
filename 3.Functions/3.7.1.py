n = int(input())
inputlst = []
for i in range(n):
    inputlst += [input().split(';')]

# Создание словаря команд
outputlst = {}
for i in range(n):
    for j in 0, 2:
        outputlst[inputlst[i][j]] = [0, 0, 0, 0, 0]

# Количество побед
for i in range(n):
    for j in 0, 2:
        outputlst[inputlst[i][j]][0] += 1

# Победы, поражения, ничьи
for i in range(n):
    if inputlst[i][1] > inputlst[i][3]:
         outputlst[inputlst[i][0]][1] += 1
         outputlst[inputlst[i][0]][4] += 3
         outputlst[inputlst[i][2]][3] += 1
    elif inputlst[i][1] == inputlst[i][3]:
        outputlst[inputlst[i][0]][2] += 1
        outputlst[inputlst[i][2]][2] += 1
        outputlst[inputlst[i][0]][4] += 1
        outputlst[inputlst[i][2]][4] += 1
    else:
        outputlst[inputlst[i][2]][1] += 1
        outputlst[inputlst[i][2]][4] += 3
        outputlst[inputlst[i][0]][3] += 1

for key in outputlst:
    print(key, end=':')
    print(*outputlst[key])
