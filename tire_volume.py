import math

width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))


volume = (math.pi * (width ** 2) * ratio * (width * ratio + (2540 * diameter) )) / 10000000
volume_rounded = round(volume, 1)


print(f"The approximate volume is {volume_rounded} cubic cm.")