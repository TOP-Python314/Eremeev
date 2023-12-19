mail = str(input())
dog = '@'

if dog in mail and mail.endswith('.ru'):
    print('да')
else:
    print('нет')
    
# sgd@ya.ru
# да

# abcde@fghij
# нет