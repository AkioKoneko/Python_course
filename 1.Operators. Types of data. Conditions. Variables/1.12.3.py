a, b = (float(input()) for _ in range(2))
oper = input()

if(oper == "pow"):
    print(a ** b)
elif(oper == "+"):
    print(a + b)
elif(oper == "-"):
    print(a - b)
elif(oper == "*"):
    print(a * b)
elif((oper == "/") and (b != 0)):
    print(a / b)
elif((oper == "mod") and (b != 0)):
    print(a % b)
elif((oper == "div") and (b != 0)):
    print(a // b)
else:
    print("Деление на 0!")
