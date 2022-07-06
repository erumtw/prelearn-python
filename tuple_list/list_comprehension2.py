# การกรองข้อมูล (filter) โดยใช้ list comprehensions

def km_mi(k):
    return k * 0.621371192

    # filter 
def v1():
    flowers = ("lily", "carnation", "iris", "sunflower", "ivy")
    #1
    n = [i.capitalize() for i in flowers if i[0] == 'i'] 
    #2
    m = [i.upper() if i[0] == 'i' else i for i in flowers]
    
    print(n)
    print(m)

def v2():
    az = [chr(i) for i in range(ord("ก"), ord("ฮ") + 1)]
    print(az)
    az2 = "-".join(az)
    print(az2)

# v1()
v2()
