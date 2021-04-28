from datetime import datetime

current = datetime.now()
weekday = current.isoweekday()

subtotal = float(input('Introduce the subtotal of your purchase: '))

if subtotal >= 50 and (weekday == 2 or weekday == 3):
    discount = subtotal * 0.1
    subtotal = subtotal - discount
    tax = subtotal * 0.06
    total = subtotal + tax
    print(f"Discount amount: ${discount:.2f}")
else:
    tax = subtotal * 0.06
    total = subtotal + tax

print(f"Sales tax amount: ${tax:.2f}")
print(f"Your total: ${total:.2f}")