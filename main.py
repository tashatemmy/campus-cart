"""
CampusCart - Campus Vendor Command Line Interface Application

An application designed to help campus vendors manage inventory, process and update shopping cart totals and generate sale receipts.

Author: Temi Odey, Python programmer
Program Scope: inventory management, update cart total, receipt generation.

"""

#login and select an option area
login_details = input("Dear user, enter your username to login to your account: ").strip().
if login_details in  ["Temi","Titi","Tayo"]:
	print(f"Welcome {login_details}, to CampusCart")
else:
	print("you need to signup to use campuscart")
user_option = int(input("Select an option: ").strip())
print(f"{login_details}, you selected option: {user_option}")

# Inventory Catalog
inventory = {
	"101": {
		"name": "Notebook",
		"price": 2.50,
		"stock": 21

	},
	"102": {
                "name": "Pen",
                "price": 1.50,  
                "stock": 15

        },
	"103": {
                "name": "Water Bottle",
                "price": 5.00,  
                "stock": 12

        },
	"104": {
		"name": "Shirt",
		"price": 8.00,
		"stock": 25
	}
}

# cart processes
cart = []
