
contacts = ['Peter', 'Parker', 21]
print(contacts)

scores = [10, 9, 8 , 7, 5]
print(sum(scores))
print(len(scores))
print(sum(scores) / len(scores))

# multidimension list
def list_demo1():
    countries = [ 
        ('th', 'Thailand'),
        ('kr', 'Korea'),
        ('jp', 'Japan')
    ]
    print(countries)
    print(countries[2])
    print(countries[0][1])

def list_demo2():
    menus = [
        ['Iced Americano', [30, 40, 50]],
        ['Iced lette', [35, 45, 55]],
        ['Water', [7]],
    ]
    print(menus)
    print(menus[0])
    print(menus[1][1])
    print(menus[1][1][2])
    
# list_demo1()
list_demo2()

