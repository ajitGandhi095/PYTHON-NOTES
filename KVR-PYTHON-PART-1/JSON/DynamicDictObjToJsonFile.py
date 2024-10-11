#Program for Saving Dict Data into the JSON File
#DynamicDictObjToJsonFile.py
import json
nor=int(input("Enter How Many Dict Object Values u have:"))
if(nor<=0):
	print("Invalid Data")
else:
	with open("emp1.json","a") as fp:
		print("---------------------------------------------------------")
		for i in range(1,nor+1):
			print("Enter {} Dict Object data".format(i))
			empno=int(input("Enter Employee Number:"))
			ename=input("Enter Employee Name:")
			sal=float(input("Enter Employee Salary:"))
			print("---------------------------------------------------------")
			#Place the above Values in dict
			d={}
			d["ENO"]=empno
			d["NAME"]=ename
			d["SAL"]=sal
			#dump object d into json file
			json.dump(d,fp)
			fp.write("\n")
			print("{} Emp Record Saved in JSON File".format(i))



