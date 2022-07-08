import pprint


def list_sort1():
    flowers = ['Aster','aconite','calla', 'lily', 'Jasmine', 'forget me not', 'Sunflower', 'ivy', 'gypso']
    
    #### sort by sorted() ####
    ## normal sort will not ignore upper/lower case
    fl = sorted(flowers) 
    print(fl)
    ## sort by ignore upper/lower case
    fl2 = sorted(flowers, key = lambda e: e.upper()) 
    print(fl2)
    ## reverse sort
    fl2r = sorted(flowers, key = lambda e: e.upper(), reverse = True)
    print(fl2r)
    
    print("-" * 100)
    #### sort by list.sort() ####
    flowers.sort()
    print(flowers)
    flowers.sort(reverse= True)
    print(flowers)
    flowers.sort(reverse= True, key= lambda e: e.upper())
    print(flowers)
    
    
def list_sort2():
    numbs = [12, 43, 13, 23, 53, 33, 1, 5, 32, 3]
    
    numbs_sorted = sorted(numbs) # น้อยไปมาก ascending, reverse = False
    numbs_sorted_r = sorted(numbs, reverse=True) # มากไปน้อย descending reversed = True

    print(numbs)
    print(numbs_sorted) 
    print(numbs_sorted_r)
    
def list_dicts_sort():
    menus = [
        {'name': 'iced latte', 'price': 120},
        {'name': 'iced mocha', 'price': 125},
        {'name': 'iced americano', 'price': 90},
        {'name': 'dirty coffe', 'price': 150}
    ]
    
    #sorted by name
    mn = sorted(menus, key= lambda e: e['name'])
    print(mn)
    
    mn2 = sorted(menus, key= lambda e: e['name'], reverse= True)
    print(mn2)

    #sort by descending price
    menus.sort(reverse= True, key=lambda e: e['price'])
    print(menus)
    #sort by ascending price
    menus.sort(reverse= False, key=lambda e: e['price'])
    print(menus)
    
    
    
# list_sort1()
# list_sort2()
list_dicts_sort()