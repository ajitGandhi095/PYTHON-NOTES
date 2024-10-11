#program obtaining the Division of Two Numbers
#DivisionDemoalternate.py
from Division import divop
from Hyd import DivsionByZeroError
while(True):
    try:
        a = int(input("Enter First Value:"))
        b = int(input("Enter Second Value:"))
        try:
            res=divop(a,b) # Function call---gives Exception or Result
        except DivsionByZeroError:
            print("\tDon't Enter Zero for Den...")
        else:
            print("Div({},{})={}".format(a,b,res))
            break
    except ValueError:
        print("\tDon't enter alnums,strs and symbols")



#Phase-3: We develop a Specific Program and
# Handling the exception if it Occurce otherwise we displayed Result