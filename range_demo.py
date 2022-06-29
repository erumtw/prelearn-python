# range(inclusive, exclusive, step)
#  
r = range(10) # -> range(0,10)
r2 = range(4, 11) # 
r3 = range(1, 22, 2) 
r4 = range(10, 0, -1)
r5 = range(-1, -11, -1)

print("type:", type(r))
print(list(r))
print("-" * 40)
print(list(r2))
print("length of r2:", len(r2))
print(list(r3))
print(list(r4))
print(list(r5))
print("sum of r3:", sum(r3))

