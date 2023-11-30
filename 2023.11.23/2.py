number = int(input())
number2 = int(input())
result = number // number2
remainder = number % number2 

if number // number2 and remainder == 0:
    print(f'{number} делится на {number2} нацело',
    f'частное: {result}',sep='\n')
elif number // number2 and remainder > 0:
    print(f'{number} не делится на {number2} нацело',
    f'неполное частное: {result}',f'остаток: {remainder}',sep='\n')

# 10
# 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1

# 8
# 2
# 8 делится на 2 нацело
# частное: 4

# 11
# 4
# 11 не делится на 4 нацело
# неполное частное: 2
# остаток: 3