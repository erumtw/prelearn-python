tupleA = 1, 5 
tupleB = (1, 15) #immutable ไม่สามารถแก้ค่าได้

# print(tupleA[0])

# tupleC = "AC", 220

# print(tupleC[0])

def distance(positionA, positionB):
    return ((positionA[0] - positionB[0]) ** 2 + (positionA[1] - positionB[1]) ** 2 ) ** .5

print("Distance between tupleA and tupleB is ", distance(tupleA, tupleB))
