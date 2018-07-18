a = input().lower().split()
b = {}

for key in a:
    if key in b:
        b[key] += 1
    else:
        b[key] = 1

for key, value in b.items():
    print(key, value)

# Ну типо я умный дофига - аргументы командной строки вывожу
import sys
for i in sys.argv:
    if(sys.argv.index(i) != 0):
        print(i)
