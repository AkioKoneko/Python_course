a = input().lower().split()
b = {}

for key in a:
    if key in b:
        b[key] += 1
    else:
        b[key] = 1

for key, value in b.items():
    print(key, value)

import sys
for i in sys.argv:
    if(sys.argv.index(i) != 0):
        print(i)
