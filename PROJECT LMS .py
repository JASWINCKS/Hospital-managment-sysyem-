alpha=True
while alpha == True:
	print("""""")
	print("""	[*] Searching for the required files.
	[*] Reqesting the MySQL server to connect.""")
	###Back End
	import mysql.connector
	mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="c_s")
	cursor=mydb.cursor(buffered=True)
	print("""	[*] The sql server is connected succesfully.""")									
	print("""
	1.Patients
	2.Staffs
	3.Billing
	4.SALARY DEATAILS
	5.Medical 
	6.exit
""")
	try:
		a= int(input("enter the option (1-6): "))				#main
		while a>= 7:
			a= int(input("only enter the option (1-6): "))
		else:	
			if a==1:												#Table name Patientsdb
				print("""
				1.register a new Patients
				2.see the data of a Patients
				3.edit the data of a Patients
				4.delete the data of a Patients
				""")
				a1= int(input("enter the option (1-4): "))
				while a >=5:
					a1= int(input("only enter the option (1-4): "))
				else:	
					if a1==1:
						a1name=(input("enter your name: "))
						try:
							a1ID=int(input("enter your ID: "))
						except:
							a1ID=int(input("enter only your ID: "))
						a1city=(input("enter your city: "))
						a1state=(input("enter your  state: "))
						a1DOB=(input("enter your DOB in the formate(YYYY-MM-DD): ")) #add date of joining also
						a1mail=(input("enter your mail id: "))
						a1CONT=int(input("enter your ph number: "))
						a1conf=input("Are you sure to enter the values?(y/n)")
						if a1conf=="y":

							try:
								a1insertstatement=("insert into Patientsdb (name,ID,City,State,DOB,Email,PHnumb)" "values (%s,%s,%s,%s,%s,%s,%s);")
								data1=(a1name,a1ID,a1city,a1state,a1DOB,a1mail,a1CONT)
								cursor.execute(a1insertstatement, data1)
								mydb.commit()
								print("values entered succesfully.")
							except:
								print("C001:some error occured in the database.")
						else:
							print("values not entered.")
										
					else:
						pass
					if a1==2:
						a1search=int(input("Enter the ID to be searched: "))
						a1searchstatement=("select * from Patientsdb where ID={};".format(a1search))
						a1result=cursor.execute(a1searchstatement)
						mydb.commit()
						for i in a1result:
							print(i)			
					else:
						pass
					if a1==3:
						print("\n1. Name")
						print("\n2. City")
						print("\n3. State")
						print("\n4. DOB")
						print("\n5. Email")
						print("\n6. PHnumb")
						choice=int(input("Enter Your Choice; "))
						if choice==1:
							field="a1name"
						if choice==2:
							field="a1city"
						if choice==3:
							field="a1state"
						if choice==4:
							field="a1DOB"
						if choice==5:
							field="a1mail"
						if choice==6:
							field="a1CONT"
						ID=int(input("Enter the id"))	
						Value=input("Enter the value: ")
						a1editsatement=('update Patientsdb set ' + field + ' = '+Value+' where a1Id = '+ID+';') 	
						a1edit=cursor.execute(a1editsatement)	
						mydb.commit()
						print("Values has been Updated")					
					else:
						print("C0001 Some Error happened in the database")
						pass
					if a1==4:
						a1delete1=int(input("Enter the ID to be deleted: "))
						a1delsatement=("DELETE FROM Patientsdb WHERE ID={};".format(a1delete1))
						cursor.execute(a1delsatement)
						mydb.commit()
						print("Deleted succesfully.")	
					else:
						print("C003:some error occured in the database.")						
			else:
				pass
			if a==2:												#Staffs
				print("""
				1.register a new staff
				2.see the data of a staff
				3.edit the data of a staff
				4.delete the data of a staff
				""")
				a2= int(input("enter the option (1-4): "))
				if a2==1:
					a2name=(input("enter staff name: "))
					a2ID=int(input("enter staff ID: "))
					a2city=(input("enter staff city: "))
					a2dep=(input("enter staff  Department: "))
					a2DOB=(input("enter staff DOB in the formate(YYYY-MM-DD): "))#add date of joining
					a2mail=(input("enter staff mail id: "))
					a2CONT=int(input("enter staff ph number: "))
					a2conf=input("Are you sure to enter the values?(y/n) ")
					if a2conf=="y":

						try:
							insertstatement2=("insert into Staff (Name,ID,City,Department,DOB,Email,PHnumb)" "values (%s,%s,%s,%s,%s,%s,%s);")
							data2=(a2name,a2ID,a2city,a2dep,a2DOB,a2mail,a2CONT)
							cursor.execute(insertstatement2, data2)
							mydb.commit()
							print("values entered succesfully.")
						except:
							print("C001:some error occured in the database.")
					else:
						print("values not entered.")
				else:
					pass
				if a2==2:
					a2search=input("enter the ID")
					searchstatement=("select * from Patientsdb where ID={};".format(a2search))
					a2result=cursor.execute(searchstatement)
					mydb.commit()
					for i in a2result:
						print(i)
				else:
					pass
				if a2==3:
					print("\n1. Name")
					print("\n2. City")
					print("\n3. State")
					print("\n4. DOB")
					print("\n5. Email")
					print("\n6. PHnumb")
					print("\n7. Department")
					choice=int(input("Enter Your Choice; "))
					if choice==1:
							field="a2name"
					if choice==2:
							field="a2city"
					if choice==3:
							field="a2state"
					if choice==4:
							field="a2DOB"
					if choice==5:
							field="a2mail"
					if choice==6:
							field="a2CONT"
					if choice==7:
						field="a2dep"		
					ID=int(input("Enter the id"))	
					Value=input("Enter the value: ")
					a2editsatement=('update staff set ' + field + ' = '+Value+' where a2Id = '+ID+';') 	
					a2edit=cursor.execute(a2editsatement)	
					mydb.commit()
					print("Values has been Updated")					
				else:
					print("C0001 Some Error happened in the database")
					pass
				if a2==4:
					a2delete1=int(input("Enter the ID to be deleted: "))
					a2delsatement=("DELETE FROM Staff WHERE ID={}".format(a2delete1))

				else:
					pass				
			else:
				pass
			if a==3:												#bill	
				print("""
				1.register a new Bill
				2.see the data of a Bill
				3.edit the data of a Bill
				4.delete the data of a Bill 
				""")
				a3= int(input("enter the option (1-4): "))
				if a3==1:
					a3name=input("Enter the Patients name: ")
					a3ID=input("Enter the bill number: ")
					a3DOB=input("Enter the date of billing in the formate(YYYY-MM-DD): ")  #billing date only
					a3city=input("Enter the name of city: ")
					a3state=input("Enter the name of state: ")
					a3Cost=input("Enter the bill amount: ")
					a3mail=input("Enter the mail id: ")
					try:
							insertstatement3=("insert into billdetails (Name,ID,City,State,DOB,Email,Cost)" "values (%s,%s,%s,%s,%s,%s,%s)")    #table name billdetails
							data3=(a3name,a3ID,a3city,a3state,a3DOB,a3mail,a3Cost)
							cursor.execute(insertstatement3, data3)
							mydb.commit()
							print("values entered succesfully.")
					except:
							print("C001:some error occured in the database.")
			         		
				else:
					pass
				if a3==2:
					a3search=input("enter the ID")
					searchstatement=("select * from billdeatails where ID={}".format(a3search))
					a3result=cursor.execute(searchstatement)
					mydb.commit()
					for i in a3result:
						print(i)
				else:
					pass
				if a3==3:
					print("\n1. Name")
					print("\n2. City")
					print("\n3. State")
					print("\n4. DOB")
					print("\n5. Email")
					print("\n6. Cost")
					choice=int(input("Enter Your Choice; "))
					if choice==1:
							field="a3name"
					if choice==2:
							field="a3city"
					if choice==3:
							field="a3state"
					if choice==4:
							field="a3DOB"
					if choice==5:
							field="a3mail"
					if choice==6:
							field="a3Cost"
					ID=int(input("Enter the id"))	
					Value=input("Enter the value: ")
					a3editsatement=('update billdetails set ' + field + ' = '+Value+' where a1Id = '+ID+';') 	
					a3edit=cursor.execute(a3editsatement)	
					mydb.commit()
					print("Values has been Updated")					
				else:
					print("C0001 Some Error happened in the database")
					pass
				if a3==4:
					a3delete=int(input("Enter the ID to be deleted: "))
					a3deletestatement=("DELETE FROM billdeatils WHERE ID={}".format(a3delete))
				else:
					pass		

			else:
				pass
			if a==4:												#SALARY DEATAIL
				print("""
				1.Register new SALARY DEATAIL.
				2.See previous SALARY DEATAIL Details.
				3.See all SALARY DEATAIL .
				4.Edid SALARY DEATAIL Details.
				5.Delete SALARY DEATAIL Details
				""")
				try:
					insertstatement4=("insert into SALARY DEATAIL (name,ID,salalry,)" "values (%s,%s,%s,%s,%s,%s,%s);")
					data4=(a4name,a4ID,a4Salary)
					cursor.execute(insertstatement4,data4)
					mydb.commit()
					print("values entered succesfully.")
				except:
					print("C001:some error occured in the database.")
				a4=int(input("Enter any option (1-5): "))
				if a4==1:
					a4name=input("Enter the SALARY DEATAIL name: ")
					a4ID=input("Enter the ID for SALARY DEATAIL:")
					a4Salary=input("Enter the price of SALARY DEATAIL: ")
				else:
					pass
				if a4==2:
					a4serch=input("Enter the ID to search: ")
					a4searchstatement=("SELECT * FROM bookdb WHERE ID={};".format(a4search))
					a4result=cursor.execute(a4searchstatement)
					mydb.commit()
					for i in a4result:
						print(i)
				else:
					pass
				if a4==3:
					a4search=input("Enter the ID to search: ")
					searchstatement=("SELECT * FROM bookdb;")
					a4result=cursor.execute(searchstatement)
					mydb.commit()
					for i in a4result:
						print(i)
				else:
					pass
				if a4==4:
					print("\n1. Name")
					print("\n2. City")
					print("\n3. State")
					choice=int(input("Enter Your Choice; "))
					if choice==1:
							field="a4name"
					if choice==2:
							field="a4salary"
					ID=int(input("Enter the id"))	
					Value=input("Enter the value: ")
					a4editsatement=('update SALARY DEATAIL set ' + field + ' = '+Value+' where a1Id = '+ID+';') 	
					a4edit=cursor.execute(a4editsatement)	
					mydb.commit()
					print("Values has been Updated")					
				else:
					print("C0001 Some Error happened in the database")
					pass
				if 	a4==5:
					a4delcon=input("Are you sure you want to delete the SALARY DEATAIL details?(y/n): ")
					if a4delcon=="y":
						a4delete=int(input("Enter the ID to be deleted:"))
						a4deletestatement=("DELETE FROM bookdb WHERE ID={};".formate(a4delete))
					else:
						pass	
			else:
				pass
			if a==5:												#Medical 
				print("""Medical """)
				print("""
				1.Register new Medical  NAME.
				2.See specific Medical   Details.
				3.See all Medical   available.
				4.Edid Medical   Details.
				5.Delete Medical   Details
				""")
				try:
					a5insertstatement=("insert into Patients (Name,ID,Price,Origin,Rating)" "values (%s,%s,%s,%s,%s,%s,%s)")
					data5=(a5name,a5ID,a5price,a5orig,a5ratig)
					cursor.execute(a5insertstatement, data5)
					mydb.commit()
					print("values entered succesfully.")
				except:
					print("C001:some error occured in the database.")
				a5=int(input("Enter any option (1-5): "))
				if a5==1:
					a5name=input("Enter the Medical name: ")
					a5ID=input("Enter the ID for Medical :")
					a5price=input("Enter the price of Medical  : ")
					a5orig=input("Enter the origin of Medical  : ")
					a5ratig=input("Enter the avg Medical  rating: ")
				else:
					pass
				if a5==2:
					a5search=int(input("enter the ID to be searched: "))
					a5searchstatement=("select * from Medical where ID={};".format(a1search))
					a5result=cursor.execute(a5searchstatement)
					mydb.commit()
					for i in a5result:
							print(i)			
				else:
					pass
				if a5==3:
					a5searchstatement=("select * from medical;")
					a5result=cursor.execute(a5searchstatement)
					mydb.commit()
					for i in a5result:
						print(i)
				else:
					pass
				if a5==4:
					print("\n1. Name")
					print("\n2. Price")
					print("\n3. Origin")
					print("\n4. Rating")
					choice=(int(input("Enter your choice")))
					if choice==1:
						field="a5name"
					if choice==2:
						field="a5price"
					if choice==3:
						field="a5origin"
					if choice==4:
						field="a5ratig"
					ID=(int(input("Enter the ID: ")))
					value=(int(input("Enter the value: ")))
					a5editstatement=('update Medical '+ field +'=' + value +'where ID={};'.format(ID))
					a5edit=cursor.execute(a5editstatement)
					mydb.commit()
					print("The values has been updated")				
				else:
					print("C0001 Some Error happened in the database")
					pass
				if 	a==5:
					a5delcon=input("Are you sure you want to delete the SALARY DEATAIL details?(y/n): ")
					if a5delcon =="y":
						a5delete=int(input("enter the id: "))
						a5deletestatement=("DELETE FROM bookdb WHERE ID={};".formate(a5delete))
			if a >= 6:												#exit
				a6=(input("Do you want to exit?(y/n): "))
				if a6=="y":
					alpha=False
				else:
					pass
	except:
		print("Error occured some where please try again.")			
else:
	print("thankyou!") 
