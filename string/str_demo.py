s = 'rainbow'
# print('rain' in s)
print('rain' not in s)

def slice():
    fname = 'ammari'
    print(fname[5])
    print(fname[0:4])
    print(fname[1::2])
    print(fname[0:5:2]) # [start:end:step]
    print(fname[-1])
    print(fname[-6:-1])
    print(fname[-1:-4:-1])
    print(fname[::-1])

def print_str(s: str):
    for i in range(len(s)):
        print("{:>3}".format(i), end = '')
    print()
    for i in range(-len(s), 0, 1):
        print("{:>3}".format(i), end = '')
    print()
    for c in s:
        print("{:>3}".format(c), end = '') # {:>3} > ชิดขวา 3 เว้น 3 ช่อง

# slice()
print_str("thaowan")
print()
s = "123456789abcdefghijklmnop"
print(s[5:10])