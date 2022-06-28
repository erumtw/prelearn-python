name = "ammari" # global scope/ module scope

def fn():
    name = "amree" # local scope
    print(name) 

def fn2():
    # name = "Mr." + name 
    print(name)

def fn3():
    global name #declare to using a global var
    name = "Mr." + name
    print(name)

print(name)
fn()
fn2()
fn3()
