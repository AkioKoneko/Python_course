p = float(3.14)

figure = input()

if (figure == "треугольник"):
    
    a, b, c = (int(input()) for _ in range(3))

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print(s)

elif (figure == "прямоугольник"):

    a, b = (int(input()) for _ in range(2))

    print(a * b)

elif (figure == "круг"):

    a = int(input())

    print(p * (a ** 2))

else:
    print("Нет такой фигуры, дурашка")
