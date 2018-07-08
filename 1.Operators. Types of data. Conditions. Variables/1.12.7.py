a = int(input())

last = a % 10
a //= 10
last += a % 10
a //= 10
last += a % 10
a //= 10

first = a % 10
a //= 10
first += a % 10
a //= 10
first += a % 10

if(first == last):
    print("Счастливый")
else:
    print("Обычный")
