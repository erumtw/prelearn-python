def composite_key_dict():
    m = {
            ("th", 2015): {"g": 15, "s": 13, "b": 17},
            ("th", 2016): {"g": 5, "s": 3, "b": 7},
            ("sg", 2015): {"g": 23, "s": 21, "b": 22},
            ("sg", 2016): {"g": 3, "s": 1, "b": 2},
            ("jp", 2015): {"g": 93, "s": 90, "b": 95},
            ("jp", 2016): {"g": 13, "s": 10, "b": 25}
        }
    
    print(m)
    print(m['th', 2015])
    print(m['th', 2015]['g'])
    
    m[("th", 2015)]['g'] = 10 
    print(m['th', 2015])
    
    m[("th", 2015)] = {"g": 5, "s": 3, "b": 7}
    print(m['th', 2015])
    
    del m[("th", 2015)]
    print(m)
    
    if ('th', 2015) in m:
        print("found")
    else:
        print(("not found"))
    
composite_key_dict()