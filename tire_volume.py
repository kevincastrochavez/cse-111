import math
from datetime import datetime

width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))


volume = (math.pi * (width ** 2) * ratio * (width * ratio + (2540 * diameter) )) / 10000000
volume_rounded = round(volume, 1)


print(f"The approximate volume is {volume_rounded} milliliters.")

current_date = datetime.now().date()

# TIRES PRICES AND INFO
# achilles = [225, 35, 20, 68.84]
# trailer_king = [175, 80, 13, 44.38]
# waterfall = [185, 60, 15, 34.41]
# super_max = [235, 70, 16, 64.91]

if width == 225 and ratio == 35 and diameter == 20:
    print('We have the Achilles for $68.84')
elif width == 175 and ratio == 80 and diameter == 13:
    print('We have the Trailer King for $44.38')
elif width == 185 and ratio == 60 and diameter == 15:
    print('We have the Waterfall for $34.41')
elif width == 235 and ratio == 70 and diameter == 16:
    print('We have the Super Max for $64.91')
else:
    print("We don't have that one available for now")

decision = input("Would you like to buy tires with the dimensions you are looking for? (Yes/No) ").lower()
if decision == 'yes':
    phone_number = input("Please introduce your phone number: ")
    print("We´ll contact you soon!")
    with open('volumes.txt', 'at') as volumes:
        print(f"{current_date}, {width}, {ratio}, {diameter}, {volume_rounded}\nPhone Number: {phone_number}", file=volumes)
else:
    print("Come back soon")
    with open('volumes.txt', 'at') as volumes:
        print(f"{current_date}, {width}, {ratio}, {diameter}, {volume_rounded}", file=volumes)


