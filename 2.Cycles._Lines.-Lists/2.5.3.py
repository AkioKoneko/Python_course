a = [int(i) for i in input().split()]

a.sort()
flag = 1

if(len(a) != 1):
    for i in range(len(a)):
        if((a[i] == a[i - 1]) and flag):
            print(a[i], end=" ")
            flag = 0
        if(a[i] != a[i - 1]):
            flag = 1
