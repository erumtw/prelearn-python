from calendar import weekday
from datetime import datetime

def demo1():
    t = [("sun", "red"), ("mon", "yellow"), ("tue", "pink"), ("wed", "green"),
         ("thu", "orange"), ("fri", "blue"), ("sat", "purple")]
    d = {}
    
    # normal
    for k, v in t:
        d[k] = v
    # print(d)
        
    # dict comprehension
    d2 = {k: v for k, v in t}
    # print(d2)
    return d2

def demo2():
    weekdays = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    weekcolors = ["red", "yellow", "pink", "green", "orange", "blue", "purple"]
    return {k.capitalize(): v for k, v in zip(weekdays, weekcolors)}

def demo3():
    dicts = demo2()
    today = datetime.now()
    print(today.strftime("%a"))
    weekdays = today.strftime("%a")
    weekcolor = dicts[weekdays]
    print(weekdays, weekcolor)

# demo1()
print(demo2())
demo3()