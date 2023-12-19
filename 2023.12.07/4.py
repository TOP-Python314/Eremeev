lot = {}

while True:
    line = input()
    if line == "":
        break
    key,value = line.split()
    lot[key] = value    

input_str = input()
result = 0

for k,v in lot.items():
    if input_str == v:
        result = int(k)

if result > 0 :
    print(result)
else:
    print('! value error !')
    
# 1000 pig
# 1001 wolf
# 1002 bear
# 1003 goat

# bear
# 1002

# 1002 apple
# 1004 banan
# 1007 mango
# 1015 lemon

# pear
# ! value error !