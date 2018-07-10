lst = [int(i) for i in input().split()]
x = int(input())

for i in range(len(lst)):
    if not (x in lst):
        print("Отсутствует")
        break
    if(x in lst[i:i + 1]):
        print(i, end=" ")
