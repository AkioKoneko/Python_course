a = [int(i) for i in input().split()]

if(len(a) == 1):
    print(a[0])
else:
    for i in range(len(a)):
        print((a[i - 1] + a[i + 1 - len(a)]), end=" ")

"""
a.insert(0, a[-1])
a.append(a[1])

print(a)

lenght = len(a)

if(lenght == 3):
    print(a[0])
else:
    for i in range(1, lenght - 1):
        print((a[i - 1] + a[i + 1]), end=" ")
"""
