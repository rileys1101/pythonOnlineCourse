nameList = []
loggedIn = False
loggedUser = 'name'
posts = []
while 1:
	option = int(input("Enter 1 to register,2 to sign in user 3 post ,4 to check post ,5 to quit"))

	if(option == 1):
		dataDisk = {}
		tmpDict = {}
		if(len(nameList) == 0):
			tmpName = input("Enter user name")
			password = input('enter password for {}'.format(tmpName))
			dataDisk['name']=tmpName
			dataDisk['password']=password
			tmpDict[str(tmpName)] = dataDisk
			nameList.append(tmpDict)
		

		elif(len(nameList)>0):
			tmpName = input("Enter user name")
			password = input('enter password for {}'.format(tmpName))
			dataDisk['name']=tmpName
			dataDisk['password']=password
			tmpDict[str(tmpName)] = dataDisk
			if(tmpDict not in nameList):
				nameList.append(tmpDict)
			elif(tmpDict in nameList):
				print('already created')

	elif(option == 2):
		loginName = input('enter name to login')
		loginPassword = input('enter your password')
		for i in nameList:
			for j in i :
				
				if(loginName==j):
					value = i[j]
					if(loginPassword == value['password']):
						loggedUser = value['name']
						print('login successful')
						loggedIn = True

					else:
						print('password incorrect')
				else:
					print('user doesnt exist please register first')
	elif(option == 3):
		if(loggedIn == False):
			print('please register first')
		else:
			print('the process of posts fo on')

	elif(option == 4):
		print(posts)


		