line = input()
result = 0
space = len(line) - line.count(" ")

for _ in range(space):           
    result += 0.30
    sres = str(result)
    
print(f'{int(result)} руб {sres[3:5]} коп')


# 11 руб 40 коп