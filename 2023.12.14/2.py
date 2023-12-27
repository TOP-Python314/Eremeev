def taxi_cost(length: int,minute = 0) -> int | None:
    
    price = 80     
    cost = (length / 150) * 6
    price += cost
    time = 0
               
    for _ in range(minute):
        time += 3
    if length == 0:
        price += 80
        price += time
        
    price += time 
    
    return int(price)


# >>> taxi_cost(1500)
# 140

# >>> taxi_cost(2560)
# 182

# >>> taxi_cost(0, 5)
# 175

# >>> taxi_cost(42130, 8)
# 1789