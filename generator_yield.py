from pickle import TRUE
from re import I


def subjext():
    yield "Physics"
    yield "Math"
    yield 'Calculas 1'
    yield 'Calculas 2'
    yield 'English'

def sum_digit(digit):
    return sum([int(i) for i in str(digit)])

def luck_num(target, start_num, end_num = 100):
    result = []
    for i in range(start_num, end_num + 1):
        if target == sum_digit(i):
            result.append(i)
    return result
            
            
def luck_num_with_generator(target, start_num):
    i = start_num
    while TRUE:
        if target == sum_digit(i):
            yield i 
        i += 1
        
        
def zip_demo():
    pretest = [2, 4, 3 , 5, 10, 8]
    posttest = [6, 5, 10, 8, 10, 9]
    z = zip(pretest, posttest)
    print(next(z))
    for i, j in z:
        print(i, j, i+j)
        
# s = subjext()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# print(luck_num(5, 1, 200))

# # 
# l = luck_num_with_generator(5, 1)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
    
zip_demo()