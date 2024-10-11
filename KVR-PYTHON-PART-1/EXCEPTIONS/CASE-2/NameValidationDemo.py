#NameValidationDemo.py
from NameValid import validation
from Names import InvalidNameError,ZeroLengthNameError
while(True):
    try:
        name=input("Enter  Name / Place / Product:")
        res=validation(name)
    except ZeroLengthNameError:
        print("\tInvalid Input--Enter Ur Name /Place / Product")
    except InvalidNameError:
        print("\t'{}' is Invalid Name--try again".format(name))
    else:
        print(res)
        break