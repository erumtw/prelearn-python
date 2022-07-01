# join(), replace() method in string

import random


def join_demo():
    station = ("HUA", "SAM", "SIL", "LUM", "KHO", "SIR",
                "SUK", "PET", "RAM", "CUL", "HUI", "SUT",
                "RAT", "LAT", "PHA", "CHA", "KAM", "BAN")
    
    # return ' -> '.join(station)
    # return " -> ".join(station[0:3])
    return " -> ".join(station[0:5][::-1])

def join_demo2(lenght: int): # generate password
    # password = ""
    # aph = list("QWERTYUIOPASDFGHJKLZXCVBNM123456789!@#$%*")
    # password = random.sample(aph, lenght)
    # return "".join(password)
    return "".join(random.sample(list("QWERTYUIOPASDFGHJKLZXCVBNM123456789@#$*"), lenght))

def replace_demo(s: str):
    return s.replace("thaowan", "like").replace("a", "@").replace("e", "3")

# print(join_demo())
print(join_demo2(10))
print(replace_demo("ammari amree thaowan"))