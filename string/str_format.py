#basic of format print
import string


def print_format():
    fname = "ammari"
    lname = "thaowan"
    nname = 'am'

    print("{} {} :{}".format(fname, lname, nname)) # {0} {1} {2}
    print("{1}, {0} :{2}".format(fname, lname, nname)) # positional

    print("-" * 100)
    a = 165456
    b = 15644.256789
    c = 123456789
    d = -5546.01

def print_format2():
    print("{}".format(a))
    print("{:,}".format(c))
    print("{:.3f}".format(b)) # จะมีการปัดเศษขึ้นลง
    print("{:,.3f}".format(b))
    print("{:15,.1f}".format(a))
    print("{:15,.1f}".format(b))
    print("{:15,.1f}".format(c))
    print("{:15,.1f}".format(d))
    print("{:=15,.1f}".format(d))


# padding in format print
def padding_format():
    print("{} {} {}".format("ammari", "thaowan", "am"))
    print("{:7}|{:8}|{:5}|".format("ammari", "thaowan", "am"))  # align left
    print("{:<7}|{:<8}|{:<5}|".format("ammari", "thaowan", "am")) 
    print("{:>7}|{:>8}|{:>5}|".format("ammari", "thaowan", "am")) # align right
    print("{:^10}|{:^11}|{:^6}|".format("ammari", "thaowan", "am"))  # align center
    print("{:*>10}|{:+^11}|{:-<5}|".format("ammari", "thaowan", "am")) # defined padding as symbol

def mult_table(n):
    for i in range(1, 13):
        print("{:3} x {:2} = {:>3}".format(n, i, n*i))

def ascii_table(start, end):
    for c in range(int(start), int(end+1)):
        print("{0:3} {0:c} {0:#08b} {0:#04o} {0:#x} {0:#X}".format(c)) # [:#] บอกสัญลักษ์ฐานด้านหน้า
        # [:c] char, [:b] binary nums, [:o] Octal num, [:x] or [:X] Hexadecimal num


def str_dict():
    data = {"fname": "ammari", "lname": "thaowan", "age": 19} # {keys: "", keys: ""}
    print("{} {} {}".format(data["fname"], data["lname"], data["age"]))
    # string format "{pos}".format("var")
    print("name:{fname:>7}{lname:>8} \nage:{age:>3}".format(**data)) 
    # formatted string f"{var}"
    print(f"name:{data['fname']:>7} {data['lname']:>8} \nage:{data['age']:>3}") 

# padding_format()
# mult_table(12)
# ascii_table(65, 90)
str_dict()
# i = "suck"
# print(f"{i}")





