a = int(input())
b = a

while(a > 99):
    a = a % 100

if(10 < a <= 19):
    print(b, "программистов")
else:
    a = a % 10
    if(a == 1):
        print(b, "программист")
    elif(2 <= a <= 4):
        print(b, "программиста")
    else:
        print(b, "программистов")
