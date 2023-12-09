numbers = []

while True:
    number = int(input())
    if number%7 == 0:
        numbers.append(number)        
    else:        
        string = ''
        for x in numbers[::-1]:
            string += str(x)+ ' '
        print(string)    
        break
        
# 7
# 7
# 14
# 21
# 23
# 21 14 7 7        