number = int(input())
score = 0

for num in range(10**(number-1),10**number):
    if num > 1:
        for i in range(2,num):  
            if num % i == 0:
                break
        else:
            score += 1

print(score)

# 3
# 143

# 4
# 1061

# 2
# 21