#ATMOperationsDemo.py
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError,WithdrawError,InSuffFundError
while(True):
	try:
		menu()
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1: 
				try:
					deposit()
				except ValueError:
					print("\tDon't enter alnums,strs and symbols for Depositing the amt:")
				except DepositError:
					print("\tDon't try to Deposit  -Ve Amount OR Zero in the account")
			case 2: 
				try:
					withdraw()
				except ValueError:
					print("\tDon't enter alnums,strs and symbols for withdraw the amount:")
				except WithdrawError:
					print("\tDon't try to withdraw  -Ve Amount OR Zero from  the account")
				except  InSuffFundError:
					print("\tUr Account does not have Suff Funds----Read Python Notes")
			case 3: 
				balenq()
			case 4: 
				print("Thx for Using Program")
				break
			case _:
				print("Ur Selection of Operation is wrong--try again")
	except ValueError:
		print("Don't Enter alnums,strs and symbols for Choice--try again")