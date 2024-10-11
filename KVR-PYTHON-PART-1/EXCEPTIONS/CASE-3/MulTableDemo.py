#MulTableDemo.py<---Main Program
from MulTable import table
from MulExcept import ZeroError,NegNumError
while(True):
    try:
        n=int(input("Enter a Number for Generating Mul Table:"))
        table(n) # Function call----gives result and exceptions
    except ValueError:
        print("\tDon't enter alnums,strs,symbols and float values")
    except ZeroError:
        print("\tDon't enter zero for Mul table")
    except NegNumError:
        print("\tDon't enter -ve number for mul table")
    except:
        print("OOOPs some thing went wrong!!!")
    else:
        print("Thx for using this Program")
        break


