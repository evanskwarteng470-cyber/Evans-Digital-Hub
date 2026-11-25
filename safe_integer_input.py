try:
    age = int(input("Enter your age: ")) 
    next_age = age + 1
    print(f"Next year, you will be {next_age}." )

except ValueError:
    print("Invalid input! Please enter a whole number.")



try:
    quantity = int(input("Enter quantity: "))
    price = 5.00

    if quantity <= 0:
        print("Quantity must be greater than zero.")
    else:
        total = price * quantity
        print(f"Total: GHS {total:.2f}")

except ValueError:
    print("Invalid input! Please Enter a valid input.")

finally:
    print("Order process completed.")








