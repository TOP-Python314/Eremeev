def deck():
    nominals = list(range(2,15))
    suit = ['черви','бубны','пики','трефы']
    
    for n in suit:
        for t in nominals:
            yield(t,n)

# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]            