a = input()
string = a.lower()
count = len(string)

count_c = string.count('c')
count_cg = string.count('g') + count_c

print(count_cg / count * 100)
