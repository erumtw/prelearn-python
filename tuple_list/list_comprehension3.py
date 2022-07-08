# การใช้ list comprehensions ในการหาผลรวมและแจกแจงความถี่

import random


def sum_by_comprehension():
    medals = [
        ['th', 10, 10, 5],
        ['jp', 12, 11, 3],
        ['kr', 5, 14, 6]
    ]
    #s = [(md[0], sum(md[1:])) for md in medals]
    
    ss = [[md[0], md[1], md[2], md[3], sum(md[1:])]for md in medals]
    # same as 
    # ss = []
    # for md in medals:
    #     ss.append([md[0], md[1], md[2], md[3], sum(md[1:])])
        
    return ss

def feq_by_comprehension():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    picker = [random.choice(flowers) for i in range (20)]
    set_of_picker = set(picker) # เก็บตัวซ้ำไว้ตัวเดียวแล้วนับจำนวนไว้ข้างใน
    
    feqs = [(i, picker.count(i)) for i in set_of_picker]
    
    return feqs

print(sum_by_comprehension())
print(feq_by_comprehension())