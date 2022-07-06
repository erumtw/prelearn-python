# print(ord("a"))
# print(chr(97))

def ascii_table():
    for i in range(0, 256):
        print(f"{i} {i:#x} {i:c} ")
        
        
# utf-8
def unicode_table():
    for i in range(ord("ก"), ord("ฮ") + 1):
        print(f"{i} {i:#x} {i:c} ")
        
def unicode_table2():
    for i in range(0xe81, 0xea0):
        print(f"{i} {i:#x} {i:c} ")
        
# ascii_table()
# unicode_table()
unicode_table2()

