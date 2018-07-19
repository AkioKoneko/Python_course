# Чтение стандартного ввода
n = int(input())
inputlst = []
for i in range(n):
    inputlst += [input().split(';')]

# Создание словаря команд
outputlst = {}
for i in range(n):
    for j in 0, 2:
        outputlst[inputlst[i][j]] = 0,0,0,0,0

print(outputlst)

# Подсчет количества игр
for i in range(n):
    for j in 0, 2:
        outputlst[inputlst[i][j]] += 1,0,0,0,0

print(outputlst)
