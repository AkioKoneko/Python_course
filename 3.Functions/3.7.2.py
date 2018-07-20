lst = {}
output1 = ''
output2 = ''

a = []
for i in input():
    a += i
b = []
for i in input():
    b += i
c = []
for i in input():
    c += i
d = []
for i in input():
    d += i

for i in range(len(a)):
    lst[a[i]] = b[i]

for i in c:
    output1 += lst[i]

tsl = {v: k for k, v in lst.items()}

for i in d:
    output2 += tsl[i]

print(output1)
print(output2)
