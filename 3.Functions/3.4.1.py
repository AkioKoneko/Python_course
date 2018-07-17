with open('input.txt') as input:
    a = input.readline()

import re
lst = re.split('(\d*)', a)

inp = str()

for i in range(2, len(lst) - 6, 4):
    inp += lst[i] * int(lst[i + 1])

with open('output.txt', 'w') as output:
    output.write(inp)
