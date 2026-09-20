"""
CampusCart - Campus Vendor Command Line Interface Application

An application designed to help campus vendors manage inventory, process and update shopping cart totals and generate sale receipts.

Author: Temi Odey, Python programmer
Program Scope: inventory management, update cart total, receipt generation.

"""

#Functions for campuscart processes
def display_catalog():
	print("\n============ CAMPUS CATALOG ==========")
	for item_id, item in inventory.items():
		print(
			f"ID: {item_id} | "
			f"Name: {item['name']} | "
			f"Price: ${item['price']:.2f} | "
			f"Stock: {item['stock']}"
		)

	print("==========================================")

def add_to_cart():
	display_catalog()
	item_id = input("Enter the product ID: ").strip()

	if item_id not in inventory:
		print("Product not found")
		return
	requested_qty = int(input(f"Enter {inventory[item_id]['name']} quantity: " ).strip())
	if requested_qty <= inventory[item_id]['stock']:
		subtotal = requested_qty * inventory[item_id]["price"]

		cart.append({
			"id": item_id,
			"qty": requested_qty,
			"subtotal": subtotal
		})
		print(f"{requested_qty} x {inventory[item_id]['name']} added to cart.")
		print(f"Subtotal: ${subtotal:.2f}")
	else:
		print(f"Unable to process cart: {inventory[item_id]['name']}  is {inventory[item_id]['stock']} left")

def view_cart():
	if not cart:
		print("your cart is empty")
	for item in cart:
		product = inventory[item["id"]]

		print(
			f"{product['name']} | "
			f"Qty: {item['qty']} | "
			f"Subtotal: ${item['subtotal']:.2f}"
		)
		print("==================================")

def cart_total():
	total = 0
	for item in cart:
		total += item["subtotal"]
	return total


def generate_receipt():
	if not cart:
		print("Your cart is empty")
	total_before_discount = cart_total()
	if total_before_discount > 20:
		discount = total_before_discount / 10
	else:
		discount = 0
	total_after_discount = total_before_discount - discount

	print("\n+-----------------------------------------+")
	print("|	    CAMPUSCART RECEIPT             |")
	print("+-----------------------------------------+")

	view_cart()
	print("----------------------------------------------")
	print(f"Subtotal:			${total_before_discount:.2f}")
	print(f"Discount:			${discount:.2f}")
	print(f"Total:				${total_after_discount:.2f}")
	print("===============================================")

	confirmation = input("Confirm checkout? (yes/no): ").strip()
	if confirmation == "yes":
		for item in cart: 
			inventory[item["id"]]["stock"] -= item["qty"]
		print("Checkout is processed!")
		print("Catalog has been updated.")
		print(f"Amount paid:	${total_after_discount:.2f}")
		cart.clear()
	elif confirmation == "no":
		print("Checkout is not processed. No change is made to your cart")
	else:
		print("Invalid response...")
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


#login user
login_details = input("Dear user, enter your username to login to your account: ").strip()
if login_details in  ["Temi","Titi","Tayo"]:
	print("===========================================================")
	print(f"Welcome {login_details}, to CampusCart CLI Application")
else:
	print(f"User not registered, please sign up to CampusCart")

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
	print("  6. Pay & Generate Receipt")
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




