# CampusCart
## Introduction
CampusCart is a command-line interface (CLI) solution designed for campus vendors to streamline products inventory management to provide  accurate sales records and tracking, cart totals and generate purchase receipt for customers.

The goal is to provide student businesses and popup vendors with a simple lightweight tool for managing everyday sales without requiring a complex point-of-sale system. 

## Problem Statement

Campus vendors often manage sales manually using notebooks, spreadsheets, calculators or memeory and this can make it difficult to:
-Track available stock accurayelt
- Calculate total items in customer carts
- Generate clear receipts
- Reduce calculation errors
- Manage transactions quickly during busy periods

CampusCart addresses offers simple business processes such as managing products, processing customer carts, calculating totals and generating receipts

## Target Audience

### student Businesses

CampusCart is designed for students selling products or services on campus including:
- Food and Snacks
- Clothing and accessories
- Beauty products 
- School supplies
- Homemade products
- Other small-scale students businesses

### Popup Vendors

This application can also support temporary or popup vendors who need a quick way to manage inventory and process transactions without setting up a full-scale point-of-sale system.

## Key Value Propositions

CampusCart provides:

1. **Simple inventory management**
   Vendors can keep track of products and available stocks

2. **Faster checkout**
   Products can be added to a customer's cart and total calculated automatically

3  **Accurate calculations**
   The application reduces manual arithmetic errors when calculating transaction totals.

4. **Receipt generation**
   Vendors can generate a clear receipt showing purchased items and the final total

5. **Lightweight CLI experience**
   CampusCart is designed to be simple and accessible from a terminal without requiring graphical interface.

6. **Designend for small vendors**
   The system focuses in the needs of student businesses and popup vendors rather than the complexity if enterprise POS systems.


## Proposed CLI Navigation

The initial application provide a simple menu-driven experience:

```text 
+----------------------------------+
|          CAMPUSCART              |
|     Campus Vendor POS CLI        |
+----------------------------------+

1. View Inventory
2. Add Product
3. Update Stock
4. Create Customer Cart
5. View Cart
6. Generate Receipt
7. View Sales
8. Exit

Select an option: __

+----------------------------------+
|        CREATE CUSTOMER CART      |
+----------------------------------+

Available Products:

1. Campus Hoodie      $35.00   Stock: 10
2. Water Bottle       $12.00   Stock: 15
3. Notebook             $5.00   Stock: 20
4. Snack Pack           $8.00   Stock: 12

Select product: 2
Enter quantity: 2

Added: Water Bottle x2
Subtotal: $24.00

1. Add Another Product
2. View Cart
3. Checkout

Select an option: _

```
 


