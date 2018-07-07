a, b, c = (int(input()) for _ in range(3))

min = a
max = a

if (b > max):
    max = b
if (c > max):
    max = c
if (b < min):
    min = b
if (c < min):
    min = c

print(max, '\n', min, '\n', ((a + b + c) - (min + max)))
