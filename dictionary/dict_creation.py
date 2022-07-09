
# # dictionary creation techniques
def demo1():
    d = {'th': 'Thailand', 'jp': 'Japan', 'kr': 'Korea'}
    print(d)

def tech1():
    en = ['Thailand', 'Japan', 'Korea']
    th = ['ไทย', 'ญี่ปุ่น', 'เกาหลีใต้']
    return dict(zip(en,th))

def tech2():
    s = list('abcdefg')
    return dict.fromkeys(s, 'alphabet')

def tech3():
    countries=[('th', 'Thailand'), ('jp', 'Japan'), ('kr', 'Korea')]
    return dict(countries)

print(tech1())
print(tech2())
print(tech3())