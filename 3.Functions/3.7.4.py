n = int(input())

_1, _2 = 0, 0

while n > 0:
    n -= 1
    a, b = input().split()
    b = int(b)
    if a == 'север':
        _2 += b
    elif a == 'восток':
        _1 += b
    elif a == 'юг':
        _2 -= b
    else:
        _1 -= b

print(_1, _2)
