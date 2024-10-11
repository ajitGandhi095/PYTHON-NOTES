#ATMOperations.py<--File Name and Module Nasme
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00 # global Variable
def deposit():
    damt=float(input("Enter the Deposit Amount:"))#implcitly raises ValueError in the case alnums,strs and symbols
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxx123 Credited with INR:{}".format(damt))
        print("Now Ur Current Bal in xxxxxx123 INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter Ur Withdraw Amount:"))#implcitly raises ValueError in the case alnums,strs and symbols
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxx123 Debited with INR:{}".format(wamt))
        print("Now Ur Current Bal in xxxxxx123 INR:{}".format(bal))
def balenq():
    print("Now Ur Current Bal in xxxxxx123 INR:{}".format(bal))


