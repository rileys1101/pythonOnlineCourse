# loops in python


# an instant variable (i) is used in a for loop to iterate through desired iterables or specific number of times


print(range(10)) 

for i in range(0,10): 
    print(i)

# here goes an example

result = 0
for i in range(1, 11): 
    result = result + i 
print("Sum of first 10 natural number :", result) 


# loops ican be iterate through itreables via value or index
a = ['apple','orange','mango']

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

