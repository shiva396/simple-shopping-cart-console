import datetime

# Sample product and discount data
# Sample product and discount data
products = [
    {
        "ProductId": 1,
        "Name": "Banana",
        "Unit": "Kg",
        "Price": 100.00
    },
    {
        "ProductId": 2,
        "Name": "Orange",
        "Unit": "Kg",
        "Price": 230.00
    },
    {
        "ProductId": 3,
        "Name": "Apple",
        "Unit": "Kg",
        "Price": 330.00
    },
    {
        "ProductId": 4,
        "Name": "Grapes",
        "Unit": "Kg",
        "Price": 230.00
    }
]

discounts = [
    {
        "DiscountId": 1,
        "ProductIds": [1],
        "Name": "Buy 1 Get 1 Free",
        "EffectiveStartDate": "2023-08-02",
        "EffectiveEndDate": "2023-08-15"
    },
    {
        "DiscountId": 2,
        "ProductIds": [2, 3],
        "Name": "Buy 2 Get 1 Free",
        "EffectiveStartDate": "2023-08-02",
        "EffectiveEndDate": None
    }
]

# Initialize shopping cart
cart = []

def apply_discount(product, quantity):
    discount = None
    for d in discounts:
        if product["ProductId"] in d["ProductIds"]:
            today = datetime.date.today()
            start_date = datetime.datetime.strptime(d["EffectiveStartDate"], "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(d["EffectiveEndDate"], "%Y-%m-%d").date() if d["EffectiveEndDate"] else None
            
            if start_date <= today and (end_date is None or today <= end_date):
                discount = d
                break
    
    if discount:
        if discount["Name"] == "Buy 1 Get 1 Free":
            return (quantity // 2 + quantity % 2) * product["Price"], discount["Name"], quantity // 2 + quantity % 2
        elif discount["Name"] == "Buy 2 Get 1 Free":
            return ((quantity // 3) * 2 + (quantity % 3)) * product["Price"], discount["Name"], (quantity // 3) * 2 + (quantity % 3)
    
    return quantity * product["Price"], "No Discount", quantity

def show_products():
    print("---------------------------------------------")
    print("Available Products:")
    print("{:<10} {:<20} {:<10}".format("ID", "Name", "Price"))
    for product in products:
        print("{:<10} {:<20} {:<10.2f}".format(product['ProductId'], product['Name'], product['Price']))
    print("---------------------------------------------")
    print("Discounts:")
    show_discounts()
    print("---------------------------------------------")
    print("(0 to go back to main menu)")

def show_discounts():
    print("{:<10} {:<20} {:<20} {:<20}".format("ID", "Name", "Products", "Validity"))
    for discount in discounts:
        product_names = ', '.join([product['Name'] for product in products if product['ProductId'] in discount['ProductIds']])
        validity = f"{discount['EffectiveStartDate']} to {discount['EffectiveEndDate']}" if discount['EffectiveEndDate'] else f"Starting from {discount['EffectiveStartDate']}"
        print("{:<10} {:<20} {:<20} {:<20}".format(discount['DiscountId'], discount['Name'], product_names, validity))

def show_cart():
    if not cart:
        print("Cart is empty.")
    else:
        print("Shopping Cart:")
        for item in cart:
            print(f"{item['product']['Name']} - Quantity: {item['quantity']} - Total Price: {item['total_price']}")
    print("(0 to go back to main menu)")

def clear_cart():
    cart.clear()
    print("Cart has been cleared.")
    print("(0 to go back to main menu)")

def calculate_total_price():
    if not cart:
        print("Cart is empty.")
    else:
        print("Shopping Cart:")
        print("{:<20} {:<10} {:<20} {:<15} {:<20}".format("Product", "Quantity", "Applied Discount", "Discounted Quantity", "Total Price"))
        for item in cart:
            total_price, discount_name, discounted_quantity = apply_discount(item['product'], item['quantity'])
            print("{:<20} {:<10.2f} {:<20} {:<10} {:<10.2f}".format(item['product']['Name'], item['quantity'], discount_name, discounted_quantity, total_price))
    print("(0 to go back to main menu)")

def main():
    while True:
        print("Main Menu:")
        print("1. Show Products")
        print("2. Show Cart")
        print("3. Clear Cart")
        print("4. Calculate Total Price")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("---------------------------------------------")
            show_products()
            print("---------------------------------------------")
            product_choice = abs(int(input("Enter the product number: ")))
            if product_choice == 0:
                continue
            selected_product = products[product_choice - 1]
            quantity = abs(float(input("Enter the quantity: ")))
            
            total_price, _, _ = apply_discount(selected_product, quantity)
            cart.append({"product": selected_product, "quantity": quantity, "total_price": total_price})
            print(f"{selected_product['Name']} added to cart.")
            print("---------------------------------------------")
        
        elif choice == "2":
            print("---------------------------------------------")
            show_cart()
            print("---------------------------------------------")
        
        elif choice == "3":
            print("---------------------------------------------")
            clear_cart()
            print("---------------------------------------------")
        
        elif choice == "4":
            print("---------------------------------------------")
            calculate_total_price()
            print("---------------------------------------------")
        
        elif choice == "5":
            print("Exiting the program.")
            break
        
        elif choice == "0":
            continue
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
