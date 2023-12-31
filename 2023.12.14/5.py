def central_tendency(n1: float, n2: float, /, *args) -> dict:
    number = sorted([n1, n2, *args])
    
    if len(number) % 2 == 0:
        median = (number[len(number)//2] + number[len(number)//2-1]) / 2
    else:
        median = number[len(number)//2]
        
    arithmetic = sum(number)/len(number)
    
    geometric = 1
    for i in number:
        geometric *= i**(1/len(number))
        
    harmonic = len(number) / sum([1/i for i in number])
    print({'median': median, 'arithmetic': arithmetic, 'geometric': geometric, 'harmonic': harmonic})
    
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}   

# >>> central_tendency(*sample)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781} 