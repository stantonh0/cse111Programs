import math
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

subtotal = float(input("What is the subtotal? "))

discount = round((subtotal * 0.10), 2)
sales_tax = round((subtotal * 0.06), 2)
total_discounted = round((subtotal - discount + sales_tax), 2)
total = subtotal + sales_tax

if subtotal >= 50:
    if day_of_week == 1 or 2:
        print(f"Your discount is {discount}")
        print(f"Your sales tax is {sales_tax}")
        print(f"Your total is {total_discounted}")
else:
    print(f"Your sales tax is {sales_tax}")
    print(f"Your total is {total}")



