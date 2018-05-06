#Car Sales man
price_base = float(input("Enter the base price of car "))
dealer_prep = float(input("Dealer prep fee is "))
destination_charge = float(input("Destination charge fee is "))
tax = price_base * 1.5
license = price_base * 0.3
total = price_base + dealer_prep + destination_charge + tax + license

print("Price of car is ", total)