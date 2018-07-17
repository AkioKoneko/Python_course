lst = []

with open("input.txt", "r", encoding='utf-8') as input:
    for line in input:
        line = line.strip().split(';')
        lst += [line]

[print(el) for el in lst]

with open('output.txt', 'w') as output:

    sumMiddle = 0
    for el in lst:
        sumMiddle = (int(el[1]) + int(el[2]) + int(el[3])) / 3

        output.write(str(sumMiddle))
        output.write('\n')

    sumMath, sumFiz, sumRus = 0, 0, 0
    sumAll = ""
    for el in lst:
        sumMath += int(el[1])
        sumFiz += int(el[2])
        sumRus  += int(el[3])
    sumMath /= len(lst)
    sumFiz /= len(lst)
    sumRus /= len(lst)
    sumAll += str(sumMath) + " " + str(sumFiz) + " " + str(sumRus)
    output.write(sumAll)
