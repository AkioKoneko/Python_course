def fib(n):                          # На вход какое по счету число нужно
    a, b = 1, 0                      # первое число 0, второе 1
    for i in range(n - 1):           # цикл пока не будет нужное по счету
        a = (a + b)                  # второе число стало суммой его и первого
        b = a - b                    # первое стало суммой - оно (вторым)
    return a                         # вернули нужное число


print(fib(int(input())))
