a = int (input())
b = int (input())
if b != 0:
    print (a / b)
else:
    print ("Division by zero")
    b = int (input ("Input non-zero value "))
    print (a / b)
