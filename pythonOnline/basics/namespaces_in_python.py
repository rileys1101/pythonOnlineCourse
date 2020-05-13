# namespace in python

a = 10 # this is global variable

def hello():
    b = 12 # this is local variable
    print(a) 

hello() # this function is accessable to to global variable a
#print(b)  this line raise an error because the local varible(b) is not accessable from global scope


print('the value of global a is ',a)

def hi():
    global a
    a = 12
hi()
print('global a value is alter by function hi()',a)
