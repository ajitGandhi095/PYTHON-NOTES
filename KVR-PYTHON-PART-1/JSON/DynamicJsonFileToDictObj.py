#Program for Reading JSON File Data into Dict Object
#DynamicJsonFileToDictObj.py
import json
try:
	with open("emp1.json","r") as fp:
			fp.seek(0)
			d=json.load(fp)
			print(d)
except FileNotFoundError:
	print("JSON File Does not Exist")