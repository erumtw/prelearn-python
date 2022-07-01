
def loop():
    for i in range(10): # for(i = 0; i < 10; i++)
        for j in range(10):
            print(i, j, sep = "-")
        print("-" * 3)

def loop_tuple():
    flowers = "lilly", "tulip", "lupin", "daisy"
    # form 1
    for flo in flowers:
        print(flo.capitalize())

    #form 2
    # for i in range(len(flowers)):
    #     print(i+1, flowers[i].capitalize(), sep = ". ")
    
def loop_str(s):
    for c in s:
        print(c.upper())

def mult_table(from_n, to_n):
    for i in range(from_n, to_n + 1):
        for j in range(1, 13):
            print(f"{i} x {j} = {i*j:.1f}") # another form of format print
        print("-" * 12)

# loop()
# loop_tuple()
# loop_str("ams d")
mult_table(2, 3)