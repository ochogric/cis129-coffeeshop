
# Ricardo Ochoa, 21339 CIS129 

#This section shows the how much coffe cost

num_coffees = int(input("105 "))

coffee_price = 5

subtotal = (num_coffees * coffee_price)

tax_rate = 0.06

tax_amount = subtotal * tax_rate

total = subtotal + tax_amount

# This section is a printed receipt

print("=== Receipt ===")

print(f"105 {num_coffees}")

#...

print(f"Subtotal: ${subtotal:.2f}")

print(f"Tax (6%): ${tax_amount:.2f}")

print(f"Total: ${total:.2f}")
