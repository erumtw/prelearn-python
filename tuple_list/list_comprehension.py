# list comprehension 

def v1():
    for i in range(1,11):
        print(f"{i:2} kg = {i* 0.6:>3.1f} miles")
        
        
def v2(): # list comprehension
    [print(f"{i:2} kg = {i* 0.6:>3.1f} miles") for i in range(1,11)]
    
    demo1 = [i * 0.6 for i in range(1,11)]
    demo2 = [[i, i * 0.6] for i in range(1,11)]
    demo3 = [kg_mi(i) for i in range(1,11)]
    
    print(demo1)
    print(demo2)
    print(demo3)
    
def v3(): # lambda
    m = list(map(lambda i: i *0.6, range(1,11)))
    print(m)



def kg_mi(k):
    return k * 0.6
    
# v1()
# v2()
v3()