a, b = (int(input()) for _ in range(2))

while (a % 3 != 0):
    a += 1

sum, count = 0, 0

for i in range(a, b + 1, 3):
    sum += i
    count += 1

print(sum / count)
