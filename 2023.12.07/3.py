number = input().split()
number2 = input().split()
number_list1 = [int(n) for n in number]
number_list2 = [int(n1) for n1 in number2]

for x in range(len(number_list1) - len(number_list2) + 1):
    if number_list1[x:x+len(number_list2)] == number_list2:
        print('да')
        break
    else:
        print('нет')
        break

# 1 2 3 4
# 1 2
# да

# 1 2 3 4
# 2 4
# нет