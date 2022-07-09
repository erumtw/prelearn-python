from distutils.command.build_scripts import first_line_re


def basic_method_set():
    fruits = {"mango", "banana"}
    ## add element ##
    # add()
    fruits.add('apple')
    # update()
    fruits.update({'papaya', 'pine apple'})
    # with | op
    fruits |= {'cherry', 'strawberry'}
    print(fruits)
    
    
    ## remove ##
    # remove() -- will error if @pm not found
    fruits.remove("cherry")
    # dicard() -- will not error if @pm not found
    fruits.discard("durian")
    # with - op
    fruits -= {"strawberry"}
    print(fruits)
    
    # search in set
    print('strawberry' in fruits)
    ## clear set ##
    fruits.clear()
    
def pass_skill(req, applicant):
    return req <= applicant

def pass_skill_atleast2(req, applicant):
    return True if len(applicant & req) >= 2 else False


basic_method_set()

req = {"Python", "R", "Java"}
applicant = {"Python", "R", "Java", "Illustrator"}
applicant2 = {"Python", "R", "CSS", "C"}
# print(pass_skill(req, applicant))
# print(pass_skill_atleast2(req, applicant2))
