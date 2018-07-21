a, b = [], []
for _ in range(int(input())):
    a += input().lower().split(' ')
for _ in range(int(input())):
    b += input().split(" ")

input = set()
for i in b:
    if i.lower() not in a:
        if i not in input:
            input.add(i)

for i in input:
    print(i)
