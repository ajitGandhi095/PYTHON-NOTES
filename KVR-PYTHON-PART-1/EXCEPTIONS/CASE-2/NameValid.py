#NameValid.py<--File Name and Module Name
from Names import InvalidNameError,ZeroLengthNameError
def validation(name): # name: Guido Va2n Rossum
    if(len(name)==0):
        raise  ZeroLengthNameError
    else:
        words=name.split() # words=[Guido, Va2n, Rossum]
        res=False
        for word in words:
            if(not word.isalpha()):
                res=True
                break
        if(res):
            raise InvalidNameError
        else:
            return "'{}' is Valid Name".format(name)


