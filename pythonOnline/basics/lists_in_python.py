# handling lists in python

a = [1,2,'hello','hi',True,False]

print(type(a))

print(len(a)) # the length of a list

print(a[0]) # The value within a list can be fetch by the index number starting from zero

del a[0]    # Index number is used to delete 

print(a)

a.remove('hi') # Deleting a value via value is also supportted

print(a)