#program obtaining the Division of Two Numbers
#DivisionDemo.py
from Division import divop
from Hyd import DivsionByZeroError
try:
    a = int(input("Enter First Value:"))
    b = int(input("Enter Second Value:"))
    res=divop(a,b) # Function call---gives Exception or Result
except DivsionByZeroError:
    print("\tDon't Enter Zero for Den...")
except ValueError:
    print("\tDon't enter alnums,strs and symbols")
else:
    print("Div({},{})={}".format(a,b,res))
finally:
    print("I am from finally Block")
    print("Program Execution Completed")

#Phase-3: We develop a Specific Program and
# Handling the exception if it Occurce otherwise we displayed Result