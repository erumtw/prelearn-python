    # ตรวจสอบหาสมาชิกใน list
def demo():
    # 1  ใช้ "" in list
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    
    def is_exsist(find):
        return find in flowers
    
    print(is_exsist("Jasmines"))
    
    # 2 use list.index("") // return index of ""
    # print(flowers.index("sunflower"))
    # print(flowers.index("sunflowers"))
    
    for i, e in enumerate(flowers):
        flowers[i] = e.capitalize()
        
    print(flowers)
    
    # การเพิ่มสมาชิก
def demo2():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "Japan", "ญี่ปุ่น"),
        ("kr", "Korea", "เกาหลีใต้")
    ]
    print(countries)
    
    # append(element)
    fr = ("fr", "France", "ฝรั่งเศส")
    countries.append(fr)
    print(countries)
    
    # insert(index, element)
    us = ("us", "USA", "อเมริกา")
    countries.insert(1, us)
    print(countries)
    
    countries.append(("sg", "Singapore", "สิงคโปร์"))
    print(countries)
    
    countries += ('ml', 'Malaysia', "มาเลเซีย")
    print(countries)
    
    
    

    
# demo()
# demo2()

# alternative ways to create list 

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(alphabet)

a = [1,5] *3
print(a)

b = [0] * 5
print(b)

print(list(b))