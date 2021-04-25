import math

manufatured_items = int(input('Enter the number of manufatured items: '))
items_per_box = int(input('Enter the number of items packed per box: '))

necessary_boxes = math.ceil(manufatured_items / items_per_box)

print(f"For {manufatured_items} items, packing {items_per_box} items in each box, you will need {necessary_boxes} boxes.")