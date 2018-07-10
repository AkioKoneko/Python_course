n = int(input())

table = [["0" for j in range(n)] for i in range(n)]

cicle = 1
ost = (n // 2 + (n % 2))
right, dawn, left, up = 0, 1, 2, 1
n1 = n2 = n3 = n4 = n
count = 1

while(cicle <= ost):

    # right
    for j in range(n1):
        table[cicle - 1][j + right] = count
        count += 1
    n1 -= 2
    right += 1

    # dawn
    for i in range(n2 - 1):
        table[i + dawn][(-cicle)] = count
        count += 1
    n2 -= 2
    dawn += 1

    # left
    for j in range(n3 - 1):
        table[(-cicle)][(-j) - left] = count
        count += 1
    n3 -= 2
    left += 1

    # up
    count -= 1
    for i in range(n4 - 1):
        table[(-i) - up][cicle - 1] = count
        count += 1
    n4 -= 2
    up += 1

    cicle += 1

for i in range(n):
    for j in range(n):
        print(table[i][j], end="\t")
    print()
