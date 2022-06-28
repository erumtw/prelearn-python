def rectangle(w, h): #dynamic typing 
    return w * h

def triangle(w, h): #function declaring
    return .5 * w * h

#main entry point
w = int(input("width = "))
h = int(input("height = "))
print("rectangle area = " + str(rectangle(w, h)))
print("triangle area = " + str(triangle(w, h)))

