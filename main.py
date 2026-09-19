"""
CampusCart - Campus Vendor Command Line Interface Application

An application designed to help campus vendors manage inventory, process and update shopping cart totals and generate sale receipts.

Author: Temi Odey, Python programmer
Program Scope: inventory management, update cart total, receipt generation.

"""

#Functions for campuscart processes
def display_catalog():
	print("displaying catalog...")
def add_to_cart():
	print("Adding item to cart")
def view_cart():
	print("view your cart")

#login user
login_details = input("Dear user, enter your username to login to your account: ").strip()
if login_details in  ["Temi","Titi","Tayo"]:
	print(f"Welcome {login_details}, to CampusCart")
else:
	print("you need to signup to use campuscart")

#campus cart main cli execution
while True:
	print("  +----------------------------------+")
	print("  |          CAMPUSCART              |")
	print("  |    Campus Vendor POS CLI         |")
	print("  +----------------------------------+")
	print("  1. View Catalog")
	print("  2. Add Product (business account only)")
	print("  3. Update Stock (business account only)")
	print("  4. Add to Cart")
	print("  5. View Cart")
	print("  6. Generate Receipt")
	print("  7. Exit")

	user_option = input("Select an option: ").strip().lower()

	if user_option == "1":
		display_catalog()
	elif user_option == "2":
		add_product()
	elif user_option == "3":
		update_stock()
	elif user_option == "4":
		add_to_cart()
	elif user_option == "5":
		view_cart()
	elif user_option == "6":
		generate_receipt()
	elif user_option == "7":
		print("You are now exiting CampusCart, See you again soon!")
		break
	else:
		print("Invalid option. Please try again")
	

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
