print("===== Welcome to Flipkart =====")

# Taking user input
product_name = input("Enter the product name: ")
price = float(input("Enter the price of the product (in ₹): "))
quantity = int(input("Enter the quantity: "))

# Calculate total bill
total = price * quantity

# Display total amount
print("\n------ BILL DETAILS ------")
print("Product Name :", product_name)
print("Price per item : ₹", price)
print("Quantity :", quantity)
print("Total Amount : ₹", total)

# Payment process
print("\nPayment Methods: 1. UPI  2. Debit Card  3. Cash on Delivery")
payment_method = int(input("Choose your payment method (1/2/3): "))

if payment_method == 1:
    print("You selected UPI Payment.")
elif payment_method == 2:
    print("You selected Debit Card Payment.")
elif payment_method == 3:
    print("You selected Cash on Delivery.")
else:
    print("Invalid payment option selected!")

print("\nThank you for shopping with Flipkart! 😊")
