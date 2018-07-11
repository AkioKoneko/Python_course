# input lst
lst = [[int(i) for i in input().split()]]

buf = input()
while (buf != "end"):
    lst.append([int(i) for i in buf.split()])
    buf = input()

lst_ = [[0 for i_ in range(len(lst[0]))] for j_ in range(len(lst))]

for i in range(len(lst)):
    for j in range(len(lst[0])):
        lst_[i][j] = (lst[i - 1][j] + lst[i - len(lst) + 1][j] + lst[i][j - 1] + lst[i][j - len(lst[0]) + 1])

for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst_[i][j], end=" ")
    print()
