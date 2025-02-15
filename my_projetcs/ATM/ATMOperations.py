#ATMOperations.py<----File Name and Module Name
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00 # Global Variable
def deposit():
	damt=float(input("Enter Ur Deposit Amount:")) # Implcitly ValueError Raises when value is alnum or symbols or pure str
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxxxxxx123 Credited with INR:{}".format(damt))
		print("Now Ur Account xxxxxxxx123 Bal INR:{}".format(bal))

def withdraw():
	wamt=float(input("Enter Ur Withdraw Amount:"))# Implcitly ValueError Raises when value is alnum or symbols or																										pure str
	global bal
	if(wamt<=0):
		raise WithdrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("Ur Account xxxxxxxx123  Debitted with INR:{}".format(wamt))
		print("Now Ur Account xxxxxxxx123 Bal INR:{}".format(bal))

def  balenq():
	print("Ur Account xxxxxxxx123 Bal INR:{}".format(bal))

