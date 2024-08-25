# PINEDA, SOPHIA KEZIAH G. ICT - 107 | PRELIM ACTIVITY | FIRST YEAR
# DECISION STRUCTURE ACTIVITY

# Computes for the total bill of customer's order

total_bill = 0

burger1 = input("Do you want burger? (Y/N) ").upper()
if burger1 == 'Y':
    burger_quantity = int(input("How many burger? "))
    total_bill += burger_quantity * 35 


pizza2 = input("Do you want a pizza? (Y/N) ").upper()
if pizza2 == 'Y':
    pizza_quantity = int(input("How many pizza? "))
    total_bill += pizza_quantity * 112  


drinks3 = input("Do you want drinks? (Y/N) ").upper()
if drinks3 == 'Y':
    drinks_quantity = int(input("How many drinks? "))
    total_bill += drinks_quantity * 15  


print(f"Your total bill is {total_bill:.1f} php")
