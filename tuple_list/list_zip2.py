# what if lengths unequal
# use itertools.cycle()

from itertools import cycle

def bmi_with_zip_uncycle():
    weight = [70, 60, 48, 50, 55] # len = 4
    height = [170, 175, 161] # len = 3
    [print(w,h) for w, h in zip(weight, height)]
    bmi = [w / (h / 100) ** 2 for w, h in zip(weight, height)]
    return bmi

def bmi_with_zip_cycle():
    weight = [70, 60, 48, 50, 55] # len = 4
    height = [170, 175, 161] # len = 3
    [print(w,h) for w, h in zip(weight, cycle(height))]
    bmi = [w / (h / 100) ** 2 for w, h in zip(weight, cycle(height))]
    return bmi

def bmi_with_zip_next():
    weight = [70, 60, 48, 50, 55] # len = 4
    height = [170, 175, 161] # len = 3
    zips_wh = zip(weight, cycle(height))
    print(next(zips_wh))
    print(next(zips_wh))
    print(next(zips_wh))
    print(next(zips_wh))
    # print(next(zips_wh))
    
    
print(bmi_with_zip_uncycle())
print("-"*100)
print(bmi_with_zip_cycle())
print("-"*100)
bmi_with_zip_next()



