# # 
# # Baisc dictionary
def dict_demo1():
    d = {'th': 'Thai', 'kr': 'Korea', 'jp': "Japan"}
    print(d)
    print(d['th'])
    print(d.keys())
    print(d.values())
    print(d.items())
    
    # add
    d['sg'] = 'Singapore'
    print(d)    
    
    # delete
    del d['th']
    print(d)

def dict_demo2():
    m = {
        "th": [5, 3, 7],
         "sg": [3, 1, 2]
    }
    
    print(m['th'])
    print(m['th'][0])
    
def dict_demo3():
    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 1, "b": 2},
        "jp": {"g": 13, "s": 10, "b": 25}
    }
    
    print(m)
    print(m['th'])
    print(m['th']['g'])
    
dict_demo1()
dict_demo2()
dict_demo3()