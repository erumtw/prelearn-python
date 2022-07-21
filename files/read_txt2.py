def reader():
    with open(r"D:\programming-learns\prelearn-python\data\nato.txt") as f:
        print("name:", f.name)
        print(f.mode)
        for line in f:
            print(line, end='')
  
def reader2():
    with open(r"D:\programming-learns\prelearn-python\data\nato.txt", mode='r') as f:
        print(f.read())

# read unicode
def reader3():
    with open(r"D:\programming-learns\prelearn-python\data\province.txt", mode='r', encoding='utf8') as f:
        print(f.read())
        
def reader_unicode():
    with open(r"D:\programming-learns\prelearn-python\data\province.txt", encoding='utf8') as f:
        # print(f.read())
        for i, j in enumerate(f):
            print(f"{i+1}. {j}", end='')
# reader()
# reader2()
# reader3()
reader_unicode()