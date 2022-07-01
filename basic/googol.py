# โปรแกรมแสดงค่า googol (1 ตามด้วยเลข 0 อีก 100 ตัว)
# Google (googol) 1e100

# form 1 
print("1" + "0"*100)
print("-" * 100)

# form 2
print("1{}".format("0"*100))
print("-" * 100)

# form 3
# f-string
print(f"1{'0'*100}")
print("-" * 100)

# form 4 
def repeat():
    print('1', end='')
    for i in range(100):
        print('0', end='')
    print()

repeat()
print("-" * 100)

# form 5 
def repeat2(ch, times):
    s = ''
    for i in range(times):
        s += ch
    return s

print('1' + repeat2('0', 100))
print("-" * 10)

#form 6 
def repeat3(ch: str, times: int):
    result = ''
    for i in range(times):
        result += ch
    return result

print("1", end='')
print(repeat3('0', 100))