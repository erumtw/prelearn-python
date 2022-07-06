# application strip(trim), isdigit

def compare_with_whitespace():
    a = "Thailand"
    b = "   Thailand            "
    # print(b.strip())
    c = "The Great"
    d = "  The Great   "
    print(a == b) 
    print(a == b.strip()) 
    print(c == d)
    print(c == d.strip())
        
def app_isdigit(n: str):
    s = ''
    for c in n:
        if c.isdigit():
            s += c
    return s

def app_isdigit2(s: str):
    total = 0
    for c in s:
        if c.isdigit():
            total += int(c)
    return total

# compare_with_whitespace()
# print(app_isdigit("(065)-045-8273  "))
print(app_isdigit2("5BT320XA"))

