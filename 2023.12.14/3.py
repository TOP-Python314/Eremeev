def numbers_strip(numbers: list, n: int=1,*,copy=False) -> list:

    numbers_copy = numbers.copy()
    
    if copy == False:
        numbers.remove(max(numbers))
        numbers.remove(min(numbers))
        return numbers
    elif copy == True:        
        for _ in numbers_copy:                  
            numbers_copy.remove(max(numbers_copy))
            numbers_copy.remove(min(numbers_copy))
        return numbers_copy  

# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True

# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False        