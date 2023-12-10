number = int(input())
fb1 = fb2 = 1
x = 0

while x < number:
    print(fb2, end=' ')
    fb1,fb2 = fb2,fb1 + fb2
    x += 1

# 11
# 1 2 3 5 8 13 21 34 55 89 144       

# 1
# 1 