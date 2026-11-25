#bundle_price = 5.00

#while True:

   # try:
       # quantity = int(input("Enter quantily: "))

       # if quantity <= 0:
         #    print("Quantity must be greater than zero.")
       # else:
           # total = bundle_price * quantity
           # print("Total: ", total) 
            #break
     
    #except ValueError:
       # print("Invalid input! Enter numbers only.")#



#sales = [15.00, 25.00, 10.00]

#total_sales = 0

#for payment in sales:

   #total_sales += payment

   # print("Total sales: GHS", total_sales)
    #break



orders =[
    {"name": "Kofi", "bundle": "2GB", "amount": 10},
    {"name": "Kojo", "bundle": "5GB", "amount": 25},
    {"name":"Ama", "bundle": "1GB", "amount": 5}
]

total_revenue = 0

for order in orders:
    total_revenue += order["amount"]

    print("Name: ", order["name"]) 

    print("Bundle: ", order["bundle"])
    
    print("Amount: ", order["amount"])

print("Total revenue: ", total_revenue)

    


    





