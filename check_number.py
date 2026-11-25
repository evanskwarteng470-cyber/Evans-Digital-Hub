while True:
    phone_number = input("Enter your phone number: ")

    if len(phone_number) == 10 and phone_number.startswith("0") and phone_number.isdigit():
        print("Valid phone number.")
        break
    else:
        print("Invalid phone number. Try again")