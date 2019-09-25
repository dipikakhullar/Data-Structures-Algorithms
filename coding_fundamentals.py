def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 


import queue 

# From class queue, Queue is 
# created as an object Now L 
# is Queue of a maximum  
# capacity of 20 
L = queue.Queue(maxsize=20) 

# Data is inserted into Queue 
# using put() Data is inserted 
# at the end 
L.put(5) 
L.put(9) 
L.put(1) 
L.put(7) 

# get() takes data out from 
# the Queue from the head  
# of the Queue 
print(L.get()) 
print(L.get()) 
print(L.get()) 
print(L.get())

#OUTPUT:
"""
5
9
1
7
"""

L.put(9) 
L.put(10) 
print("Full: ", L.full()) 
  
print(L.get()) 
print(L.get()) 
print(L.get()) 
  
# Return Boolean for Empty 
# Queue 
print("Empty: ", L.empty()) 
  