number = int(input())
fb1 = fb2 = 1
x = 0

while x < number:
    fb1,fb2 = fb2,fb1 + fb2
    x += 1
    print(fb2, end=' ')    