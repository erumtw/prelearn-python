def list_iterate():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    
    # for flower in flowers:
    #     print(flower)
        
    # for i in range(len(flowers)):
    #     print(f"{i+1} {flowers[i]}")
    for i, e in enumerate(flowers):
        print(f"{i+1} {e}")
        
        
def list_iterate2():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "Japan", "ญี่ปุ่น"),
        ("kr", "Korea", "เกาหลีใต้")
    ]
    
    for i, e in enumerate(countries):
        # print(f"{countries}")
        print(f"{i+1} {e[1]}")
        
# list_iterate()
list_iterate2()