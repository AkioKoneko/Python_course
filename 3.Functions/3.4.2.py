text = open('input.txt').read().replace('\n', ' ').lower().split()
text = sorted(text)

count = 0
a = ''

for i in text:
    if(text.count(i) > count):
        count = text.count(i)
        a = i

inp = a + " " + str(count)

with open('output.txt', 'w') as output:
    output.write(inp)
