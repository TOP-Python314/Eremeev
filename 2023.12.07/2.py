list_fruit = []


while True:    
    fruit = str(input())
    list_fruit.append(fruit)
    if fruit == '':
        break
    


if len(list_fruit) == 2:
    print(str(list_fruit[0]))
else:
    print(', '.join(list_fruit[0:-2]), 'и' ,''.join(list_fruit[-2:-1]))    






# яблоко
# манго
# апельсин

# яблоко, манго и апельсин

# яблоко

# яблоко