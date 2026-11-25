def calculate_discount(price, discount):
    discount = (discount/100) * price
    final_price = price - discount

    return final_price

final_price = calculate_discount(200, 15)
print(final_price)


def display_bundles():
    print("\n ====== EVANS DIGITAL HUB ======")
    print("Available MTN Data Bundles")
    print("1. 1GB - GHS 5.00") 
    print("2. 2GB - GHS 9.70")
    print("3. 3GB - GHS 14.50")
    print("4. 4GB - GHS 19.00")
    print("5. 5GB - GHS 24.00")
    print("6. 6GB - GHS 28.00")
    print("7. 8GB - GHS 37.50") 
    print("8. 10GB - GHS 44.50")
    print("9. 15GB - GHS 63.00")
    print("10. 20GB - GHS 85.00")
    print("11. 25GB GHS 115.00")
    print("12. 30GB GHS 127.00")

display_bundles()

print("\nCustomer 2 is viewing the bundles...")
display_bundles()

def get_bundle_price(bundle):
    if bundle == "1GB":
        return 5.00
    elif bundle == "2GB":
        return 9.70
    elif bundle == "3GB":
        return 14.50
    elif bundle == "4GB":
        return 19.00
    elif bundle == "5GB":
        return 24.00
    elif bundle == "6GB":
        return 28.00
    elif bundle == "8GB":
        return 37.50
    elif bundle == "10GB":
        return 44.50
    elif bundle == "15GB":
        return 63.00
    elif bundle == "20GB":
        return 85.00
    elif bundle == "25GB":
        return 115.00
    elif bundle == "30GB":
        return 127.00
    else:
        return None

price = get_bundle_price("5GB")

if price is not None:
    print(f"Price: GHS {price:.2f}")
else:
    print("Bundle not available.")


def welcome_customer(name):
    print("\nWelcome to Evans Digital Hub,", name)
    print("Thank you for choosing us!")

welcome_customer("Evans")
welcome_customer("John")

def validate_phone_number(phone_number):
    if len(phone_number) == 10 and phone_number.startswith("0") and phone_number.isdigit():
        return True
    else:
        return False

print(validate_phone_number("0241234567"))
print(validate_phone_number("12345"))


def save_order(order_id,customer_name, bundle, price, phone_number):
    with open("orders.txt", "a") as file:
        file.write(f"\nOrderID: {order_id}\n")
        file.write(f"\nCustomer: {customer_name}\n")
        file.write(f"\nBundle: {bundle}\n")
        file.write(f"\nPrice: GHS {price:.2f}\n")
        file.write(f"\nRecipient: {phone_number}\n")
        file.write(f"\n------------------------------\n")

print("Order saved successfully!") 

def generate_order_id():
    with open("order_counter.txt", "r" ) as file:
        order_number = int(file.read())

    order_number += 1

    with open("order_counter.txt", "w") as file:
        file.write(str(order_number))

    order_id = f"EDH{order_number:03d}"
    return order_id

def process_order():
    while True:
            customer_name = input("Enter customer name: ")
            if customer_name == "":
                print("Name cannot be empty. Please try again.")
                continue
            break
    welcome_customer(customer_name)
    display_bundles()

    while True:
        bundle = input("Enter your preffered bundle (e.g. 5GB): ").upper().strip()

        price = get_bundle_price(bundle)

        if price is None:
           print("Invalid bundle selection. Please try again.")
           continue

        break
    
    print(f"\nSelected bundle:{bundle}")
    print(f"Price: GHS {price:.2f}")

    while True:
        phone_number = input("Enter recipient phone number: ").strip()

        if not validate_phone_number(phone_number):
         print("Invalid phone number! Please try again")
         continue

        break
    
    
    

    order_id = generate_order_id()
    save_order(order_id, customer_name, bundle, price, phone_number)

        

process_order()



    













