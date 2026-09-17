"""
CampusCart - Campus Vendor Command Line Interface Application

An application designed to help campus vendors manage inventory, process and update shopping cart totals and generate sale receipts.

Author: Temi Odey, Python programmer
Program Scope: inventory management, update cart total, receipt generation.

"""

login_details = input("Dear user, enter your username to login to your account: ").strip().
if login_details in  ["Temi","Titi","Tayo"]:
	print(f"Welcome {login_details}, to CampusCart")
else:
	print("you need to signup to use campuscart")
user_option = int(input("Select an option: ").strip())
print(f"{login_details}, you selected option: {user_option}")
