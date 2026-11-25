print("Welcome to Evans Digital Hub! ")

customer_name = input("Please enter your name: ")
print("Hello, ", customer_name )
print("Thank you for choosing Evans Digital Hub!")

print("AVAILABLE SERVICES.")
print("1. MTN Data Bundles")
print("2. Check prices")
print("3. Exit")

choice = input("Choose an option: ")

if choice == "1":
    print("\n---MTN DATA BUNDLES---")
    print("1.   1GB   - GHS 5.00")
    print("2.   2GB   - GHS 9.70")
    print("3.   3GB   - GHS 14.50")
    print("4.   4GB   - GHS 19.00")
    print("5.   5GB   - GHS 24.00")
    print("6    6GB   - GHS 28.00")
    print("7.   8GB   - GHS 37.50")
    print("8.   10GB   - GHS 44.50")
    print("9.   15GB  - GHS 63.00")
    print("10.   20GB  - GHS 85.00")
    print("11.  25 GB - 115.00")
    print("12.  30 GB  127.00")

    bundle_choice = input("\nChoose a bundle (1-12 ):")
    print("DEBUG:",repr(bundle_choice))

    selected_bundle = ""
    selected_price = 0.00

    if bundle_choice == "1":
        selected_bundle = "1GB"
        selected_price = 5.00
        print("You selected 1GB.")
        print("price: GHS 5.00")

    elif bundle_choice == "2":
        selected_bundle = "2GB"
        selected_price = 9.70 
        print("You selected 2GB.")
        print("Price: GHS 9.70")

    elif bundle_choice == "3":
          selected_bundle = "3GB"
          selected_price = 14.50
          print("You selected 3GB.")
          print("price: GHS 14.50")

    elif bundle_choice == "4":
          selected_bundle = "4GB"
          selected_price = 19.00
          print("You selected 4GB.") 
          print("priced: GHS 19.00") 

    elif bundle_choice == "5":
          selected_bundle = "5GB"
          selected_price = 24.00
          print("You selected 5GB.")
          print("Price: GHS 24")

    elif bundle_choice == "6":
          selected_bundle = "6GB"
          selected_price = 28.00
          print("You selected 6GB.")
          print("Price: GHS 28")

    elif bundle_choice == "7":
          selected_bundle = "8GB"
          selected_price = 37.50
          print("You selected 8GB.")
          print("Price: GHS 37.50")

    elif bundle_choice == "8":
          selected_bundle = "10GB"
          selected_price = 44.50
          print("You selected 10GB.")
          print("Price: GHS 44.50")

    elif bundle_choice == "9":
          selected_bundle = "15GB"
          selected_price = 63.00
          print("You selected 15GB.")
          print("Price: GHS 63.00")

    elif bundle_choice == "10":
          selected_bundle ="20GB"
          selected_price = 85.00
          print("You selected 20GB.")
          print("Price: GHS 85.00")

    elif bundle_choice == "11":
          selected_bundle = "25GB"
          selected_price = 115.00
          print("You selected 25GB")
          print("Price: GHS 115.00")

    elif bundle_choice == "12":
          selected_bundle = "30GB"
          selected_price = 127.00
          print("You selected 30GB.")
          print("price: GHS 127.00")

    else:
        print("This bundle selection is not available yet")

    print("DEBUG BUNDLE:", repr(selected_bundle))

    if selected_bundle != "":
          while True:
            phone_number = input("Enter recipient's phone number: ")
            if len(phone_number) == 10 and phone_number.startswith("0") and phone_number.isdigit():
                  print("Valid phone number!")
                  break
            else:
                  print("Invalid phone number. Please try again.")

    print("\n ====== ORDER SUMMARY =====")
    print("Customer: ", customer_name)
    print("Bundle: ", selected_bundle)
    print(f"Price: GHS {selected_price:.2f}")
    print("Recipient: ", phone_number)
    print("Thank you for choosing Evans Digital Hub!")

    with open("Oders.txt", "a") as file:
          file.write(f"\nCustomer: {customer_name}\n")
          file.write(f"\nBundle: {selected_bundle}\n")
          file.write(f"\nPrice: GHS {selected_price:.2f}\n")
          file.write(f"\n Recipient: {phone_number}\n")
          file.write("------------------------------------------------\n")
    print("Order saved succesfully!")


elif choice == "2":
        print("You selected check prices!")
elif choice == "3":
        print("Thank you for visiting Evans Digital Hub!")
else:
        print("Invalid choice. Please try again.")

    