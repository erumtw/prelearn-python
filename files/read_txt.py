def read_file():
    f = open(r"D:\programming-learns\prelearn-python\data\nato.txt")
    data = f.read()
    print(data)
    f.close()

def read_line():
    f = open(r"D:\programming-learns\prelearn-python\data\nato.txt")
    data = f.readline()
    print(data, end="")
    data2 = f.readline()
    print(data2)
    f.close()

def read_liness():
    f = open(r"D:\programming-learns\prelearn-python\data\nato.txt")
    data = f.readlines()
    print(data, end="")
    f.close()

def read_line2():
    # read first 3 line
    f = open(r"D:\programming-learns\prelearn-python\data\nato.txt")
    for i in range(3):
        print(f.readline(), end='')
    f.close()

def read_line3():
    # read first 3 line
    f = open(r"D:\programming-learns\prelearn-python\data\nato.txt")
    for i in f:
        print(i.upper(), end='')
    f.close()
    

# read_file()
# read_line()
# read_liness()
# read_line2()
read_line3()