year = int(input())
residue = year % 100
division = year % 400
divide = year % 4

if year // 4 and residue > 0 and divide == 0 or division == 0:
    print('да')
else:
    print('нет')
    
# 2020
# да

# 2023
# нет