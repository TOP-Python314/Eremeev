code = input()
codes = {'0b','b','01','10'}

for c in codes:
    if code.startswith(c):
        print('да')
        break
    else:
        print('нет')
        break

# b11
# да       

# 1b0101
# нет