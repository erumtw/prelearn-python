def dict_iterate():
    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 1, "b": 2},
        "jp": {"g": 13, "s": 10, "b": 25}
    }
    
    for d in m: # same as m.keys()
        print(d)
        
    for d in m.keys():
        print(d)

    for f in m.values():
        print(f)
        
    for d in m.items():
        print(d)

    for k, v in m.items():
        print(f"keys = {k}: values = {v}")
        
dict_iterate()