def modify_list(l):
    count = len(l) - 1
    while(count >= 0):
        if((l[len(l) - 1] % 2) != 0):
            l.pop()
        else:
            l.insert(0, (l[len(l) - 1] // 2))
            l.pop()
        count -= 1


# test
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
