# functions in python

def Hello():
    print('this is function execution')
    return 'this is function output'


print(Hello())


# function parameter 
def sum(x):
    print(x)
    return x + 3

print(sum(2))

def mainFun():
    print('this is main function')
    def nested():
        print('this is nested function')
    nested()

mainFun()
