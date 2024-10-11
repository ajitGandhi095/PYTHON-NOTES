#OopsEmp.py<------File Name and Module Name
class Employee:
	def getempvals(self,eno,ename,sal):
		self.eno=eno
		self.name=ename
		self.sal=sal
	def dispempvals(self):
		print("\t{}\t{}\t{}".format(self.eno,self.name,self.sal))
