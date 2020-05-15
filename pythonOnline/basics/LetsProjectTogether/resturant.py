# resturant project

# functions

# 1 name register
# 2 menu
# 3 order
# 4 quit
nameList=[]
menu = ['apple','orange','banana']
orderDict= {}
while(True):
    order = []
    option = int(input("Enter 1 to register,2 for menu,3 to order 4 to quit"))
    if(option == 1):
        name = input('Enter your name')
        nameList.append(name)
        print(nameList)
    elif(option == 2):
        print('Here comes the menu')
        for i in menu:
            print(i)
    elif(option == 3):
        while(True):
            food = input('enter food name to order and q to quit')
            if(food == 'q'):
                #here
                currentuser=nameList[-1]
                orderDict[str(currentuser)]=order
                print(orderDict)
                break
            else:
                order.append(food)
                print(order)

    elif(option==4):
        break
    else:
        print('please ony enter number between 0 to 5')
