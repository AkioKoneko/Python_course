a = int(input())

a1 = a % 10

a2 = (a % 100) // 10

a3 = (a % 1000) // 100

a4 = (a % 10000) // 1000

a5 = (a % 100000) // 10000

a6 = a // 100000

if(a1 + a2 + a3 == a4 + a5 + a6):
    print("Счастливый")
else:
    print("Обычный")

'''
sum1, sum2 = 0, 0;

while(a > 999):
    sum1 += a % 10
    a //= 10
while(a > 0):
    sum2 += a % 10
    a //= 10

if(sum1 == sum2):
    print("Счастливый")
else:
    print("Обычный")
'''
