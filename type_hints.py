#type hints 

# parameter hint
def information(name: str, age: int, sex: str): #just type hint for ide to easier intelligence, not fixed type still can param another type
    name = name.upper()
    age.bit_length()
    sex = sex.lower()
    print(name, age, sex)

# information("ammari", 10, "Men")

# return type hint
def upper(fname: str, lname) -> str:
    return fname.upper(), lname.upper()


class Person:
    def __init__(self, fname, lname, age, sex):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex

    def get_information(self):
        return self.fname, self.lname, self.age, self.sex

def register(p: Person):
    
    print(p.get_information())

person = Person("Ammari", "Thaowan", 19, "Male")

register(person)