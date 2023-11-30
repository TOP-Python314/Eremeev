cage = input()
cage2  = input()

if (ord(cage[0]) + int(cage[1])) % 2 == 0 == (ord(cage2[0]) + int(cage2[1])) % 2 == 0:
    print('да')
elif (ord(cage[0]) + int(cage[1])) % 2 > 0 == (ord(cage2[0]) + int(cage2[1])) % 2 > 0:
    print('да')
else:
    print('нет')
    
# a1
# b2
# да

# a1
# b1
# нет
