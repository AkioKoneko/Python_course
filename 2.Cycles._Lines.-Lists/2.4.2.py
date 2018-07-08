input = input()
now = ""
last = input[0]
count = 0

# aaaabbasdddd

for i in input:
    now = i
    if(last == now):
        count += 1
    elif(last != now):
        print(last, end="")
        print(count, end="")
        count = 1
    last = now
print(last, end="")
print(count, end="")
