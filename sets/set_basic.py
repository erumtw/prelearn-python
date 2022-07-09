# set เป็นได้ทั้ง mutable immutable ขุึ้นอยู่กับการประกาศ 
#  
def basic1():
    countries = {'Thailand', 'Korea', 'Japan'} # mutable
    print(countries)
    
    # voidset = {} # ประกาศแบบนี้จะ้เป็น dictionary
    voidset = set()
    
    voidset.add('one') # add() เพิ่มได้ทีละตัว
    print(voidset)
    
    voidset.update({'two', 'three'}) # update() ได้หลายตัว 
    print(voidset)
    
    
def basic2():
    # ใน set ใส่ได้แค่เดี่ยวๆ กับ tuple เท่านั้น list, dict ไม่ได้
    xy = {(1, 2), (3, 5), (5, 3)} # tuple -> immutable -> hashable
    
    # error if list in set
    # countries = {["Thailand", "Bangkok"], ["Japan", "Tokyo"]}   # list -> mutable -> unhashable
    
    print(xy)
    xy.update({(2,1)})
    print(xy)

def basic_op():
    a = {"mango", "banana", "coconut", "mango", "apple"}
    b = {"cherry", "mango", "apple"}
    
    print(a)
    
    # union | 
    print(a | b) 
    
    # intersect &
    print(a & b)
    
    # -
    print(a - b)
    
    # symmetric difference  (a union b) - (a intersect b)
    print(a ^ b)
    
# basic1()
# basic2()
basic_op()
