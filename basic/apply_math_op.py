def leap_year(year):
    return True if year % 4 == 0 else False
    # if year % 4 == 0:
    #     return True
    # else:
    #     return False

def leap_year_bhuddist(year):
    # return True if year % 4 == 0 else False
    if year % 4 == 3:
        return True
    else:
        return False

def is_even(num):
    return True if num % 2 == 0 else False

def is_odd(num):
    return not(is_even(num))

def promotion(come, pay, per_head, pax): #pax: amount of costumer com x pay y
    return ((pax // come) * (pay * per_head)) + ((pax % come) * per_head)

# print(leap_year(2016))
# print(leap_year_bhuddist(2564))
# print(is_even(10))
# print(is_odd(10))
print(promotion(4, 3, 199, 5))