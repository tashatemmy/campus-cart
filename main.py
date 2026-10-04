"""
CampusCart - Campus Vendor POS CLI

Integrates:
- inventory.py: inventory and stock management
- cart.py: cart and receipt processing
- logger.py: transaction auditing
"""

from inventory import (
    display_catalog,
    verify_stock,
    update_stock,
    calc_price_quote,
    filter_available_products,
    sort_product_by_price
)

from cart import (
    add_to_cart,
    calculate_subtotal,
    stream_receipt_lines
)

from logger import log_transaction, get_audit_summary


# Inventory data
inventory = {
    "101": {"name": "Notebook", "price": 2.50, "stock": 21},
    "102": {"name": "Pen", "price": 1.50, "stock": 15},
    "103": {"name": "Water Bottle", "price": 5.00, "stock": 12},
    "104": {"name": "Shirt", "price": 8.00, "stock": 25}
}

cart = []


def add_product(inventory):
    """Add a new product to the inventory."""

    item_id = input("Enter new product ID: ").strip()

    if item_id in inventory:
        print("Product ID already exists.")
        return

    name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter product price: ").strip())
        stock = int(input("Enter product stock: ").strip())
    except ValueError:
        print("Invalid price or stock value.")
        return

    if price < 0 or stock < 0:
        print("Price and stock cannot be negative.")
        return

    inventory[item_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print(f"{name} added successfully.")


def update_inventory_stock(inventory):
    """Update the stock quantity for an existing product."""

    display_catalog(inventory)

    item_id = input("Enter product ID: ").strip()

    if item_id not in inventory:
        print("Product not found.")
        return

    try:
        quantity = int(
            input(
                "Enter stock change "
                "(use a negative number to decrease stock): "
            ).strip()
        )
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if update_stock(inventory, item_id, quantity):
        print(
            f"Stock updated. "
            f"New stock: {inventory[item_id]['stock']}"
        )
    else:
        print("Unable to update stock.")


def add_cart_item(cart, inventory):
    """Collect user input and add a product to the cart."""

    display_catalog(inventory)

    item_id = input("Enter the product ID: ").strip()

    if item_id not in inventory:
        print("Product not found.")
        return

    try:
        quantity = int(
            input(
                f"Enter {inventory[item_id]['name']} quantity: "
            ).strip()
        )
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if not verify_stock(inventory, item_id, quantity):
        print(
            f"Unable to add product. "
            f"Available stock: {inventory[item_id]['stock']}"
        )
        return

    if add_to_cart(cart, inventory, item_id, quantity):
        quote = calc_price_quote(
            inventory[item_id],
            quantity
        )

        print(
            f"{quantity} x {inventory[item_id]['name']} "
            f"added to cart."
        )
        print(f"Subtotal: ${quote['subtotal']:.2f}")


@log_transaction
def checkout(cart, inventory):
    """Generate the receipt and process checkout."""

    if not cart:
        print("Your cart is empty.")
        return

    subtotal = calculate_subtotal(cart)

    discount_rate = 0.10 if subtotal > 20 else 0

    # Use the inventory pricing function for the final quote.
    first_item = inventory[cart[0]["id"]]

    if len(cart) == 1:
        quote = calc_price_quote(
            first_item,
            cart[0]["qty"],
            discount_rate=discount_rate
        )

        discount = quote["discount"]
        total = quote["total"]

    else:
        discount = subtotal * discount_rate
        total = subtotal - discount

    print("\n+-----------------------------------------+")
    print("|           CAMPUSCART RECEIPT            |")
    print("+-----------------------------------------+")

    for line in stream_receipt_lines(cart, inventory):
        print(line)

    print(f"Discount: ${discount:.2f}")
    print(f"Total: ${total:.2f}")

    confirmation = input(
        "Confirm checkout? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        for item in cart:
            update_stock(
                inventory,
                item["id"],
                -item["qty"]
            )

        print("Checkout processed successfully.")
        print(f"Amount paid: ${total:.2f}")

        cart.clear()

    elif confirmation == "no":
        print("Checkout cancelled. No changes were made.")

    else:
        print("Invalid response. Checkout was not processed.")


def view_cart(cart, inventory):
    """Display the current cart."""

    if not cart:
        print("Your cart is empty.")
        return

    for line in stream_receipt_lines(cart, inventory):
        print(line)


def show_inventory_options(inventory):
    """Demonstrate Lambda-based filtering and sorting."""

    available = filter_available_products(inventory)
    sorted_products = sort_product_by_price(inventory)

    print("\nAvailable Products:")
    for product in available:
        print(
            f"{product['name']} - "
            f"${product['price']:.2f} - "
            f"Stock: {product['stock']}"
        )

    print("\nProducts Sorted by Price:")
    for product in sorted_products:
        print(
            f"{product['name']} - "
            f"${product['price']:.2f}"
        )


def main():
    """Run the CampusCart CLI."""

    login_details = input(
        "Dear user, enter your username to login "
        "to your account: "
    ).strip()

    if login_details in ["Temi", "Titi", "Tayo"]:
        print(
            "==========================================================="
        )
        print(
            f"Welcome {login_details}, "
            "to CampusCart CLI Application"
        )
    else:
        print(
            "User not registered, please sign up to CampusCart."
        )
        return

    while True:

        print("\n+----------------------------------+")
        print("|           CAMPUSCART            |")
        print("|      Campus Vendor POS CLI      |")
        print("+----------------------------------+")
        print("1. View Catalog")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Pay & Generate Receipt")
        print("7. View Inventory Options")
        print("8. Exit")

        user_option = input(
            "Select an option: "
        ).strip().lower()

        if user_option == "1":
            display_catalog(inventory)

        elif user_option == "2":
            add_product(inventory)

        elif user_option == "3":
            update_inventory_stock(inventory)

        elif user_option == "4":
            add_cart_item(cart, inventory)

        elif user_option == "5":
            view_cart(cart, inventory)

        elif user_option == "6":
            checkout(cart, inventory)

        elif user_option == "7":
            show_inventory_options(inventory)

        elif user_option == "8":
            print(
                "You are now exiting CampusCart. "
                "See you again soon!"
            )
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
