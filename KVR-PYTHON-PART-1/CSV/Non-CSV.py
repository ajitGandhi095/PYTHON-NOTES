#Program for Reading the Data from CSV File
#Non-CSV.py
try:
	with open("E:\\KVR-PYTHON-6PM\\FILES\\NOTES\\student.csv","r") as fp:
		csvdata=fp.read()
		print("-"*50)
		print("CSV File Data")
		print("-"*50)
		print(csvdata)
		print("-"*50)
except FileNotFoundError:
	print("File Does not Exist")