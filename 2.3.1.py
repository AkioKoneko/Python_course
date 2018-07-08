a, b, c, d = (int(input()) for _ in range(4))

# Вывод первой строки с табуляцией в начале
print("\t", end="")
for i in range(c, d + 1):
    print(i, end="\t")
print()

# Вывод остальных строк
for j in range(a, b + 1):
    print(j, end="\t")
    for k in range(c, d + 1):
        print(k * j, end="\t")
    print()
