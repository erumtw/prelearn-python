# application upper lower and title method 
def app_upper_lower():
    s = input("[Y]es or [N]o: ")

    # if s.lower == 'y' or
    if s.upper == "Y": # simplified than s == "y" or s == "Y"
        print("Yes sir!")
    else:
        print("bro, y?")

def split_demo():
    s = "The great Ammari"
    print(s + " --> ", end="")
    print(s.split())

    ss = "mocha,latte,americano"
    print(ss + " --> ", end="")
    print(ss.split(","))

    name = s.split()[2]
    print(name)

    a, b, c = ss.split(",")
    print(a, b, c)

def app_split():
    fname, lname = input("Enter Your Full name: ").split()
    print("first name:".title(), fname.capitalize())
    print("Last Name:", lname.capitalize())

# print("the land of smile".title())
# prompt()
# split_demo()
# app_split()




