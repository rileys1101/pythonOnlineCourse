# namespace in python

a = 10 # this is global variable

def hello():
    b = 12 # this is local variable
    print(a) 

hello() # this function is accessable to to global variable a
print(b) # this line raise an error because the local varible(b) is not accessable from global scope
