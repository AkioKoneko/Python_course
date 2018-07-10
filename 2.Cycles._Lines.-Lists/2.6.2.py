a = int(input())
count = 1
n = []

while(len(n) < a):
    n += [count] * count
    count += 1

print(*n[0:a])
