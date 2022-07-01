
# while loop
from tkinter import N


def sum_input():
    n = int(input("Enter number: "))
    total = 0
    while n != 0:
        total += n
        n = int(input("Enter number: "))
    return total

# repeat until as know as do...while
def sum_input2():
    total = 0
    while True: 
        n = int(input("Enter number: "))
        if n != 0:
            total += n
        else:   
            break
    return total

# print("total =", sum_input())
print("total =", sum_input2())