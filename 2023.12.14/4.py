def countable_nouns(year: int, years: tuple[str, str, str]) -> str:

    year_s = str(year)
    if year != 11 and year_s.endswith('1'):
        return years[0]
    elif year_s.endswith('2') and year != 12 or year_s.endswith('3') and year != 13    or year_s.endswith('4') and year != 14:
        return years[1]
    else:
        return years[2]

# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'        