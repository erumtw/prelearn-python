def demo_loop():
    s = {"apple", "banana", "mango", "cherry"}
    # unsort
    for i in s:
        print(i)
    
    #sort
    l = list(s)
    l.sort
    [print(i) for i in l]
    
def demo_loop2():
    countries = {
        ("th", "Thailand"),
        ("jp", "Japan"),
        ("kr", "Korea")
    }
    # # unsort
    # [print(i) for i in countries]
    # [print(i[0]) for i in countries]
    
    # # sort
    # sort_countries = list(countries)
    # sort_countries.sort()
    # [print(i) for i in sort_countries]
    # [print(i[0]) for i in sort_countries]
    
    # iterate loop ways
    ## method 1
    [print(i) for i in countries]
    ## method 2
    [print(f"{id} {name}") for id, name in countries]
    ## method 3
    [print(f"{i+1}. {id} {name}") for i, (id, name) in enumerate(countries)]


def immutable_set(): # frozenset
    imset = frozenset(['lily', 'rose'])
    print(imset)
    
# demo_loop()
# demo_loop2()
immutable_set()