import math

def main():
  with open('can.txt') as can_file:
      for line in can_file:
          name = line.strip()
          radius = line.strip()
          height = line.strip()
          price = line.strip()

          can_name = name[0].strip()
          can_radius = radius[1].strip()
          can_height = height[2].strip()
          can_price = price[3].strip()

          print(can_name)
          print(can_radius)
          print(can_height)
    
    
def cylinder_volume(radius, height):
  return math.pi * radius ** 2 * height
  

def surface_area(radius, height):
  return 2 * math.pi * radius * (radius + height)
  
def find_storage(volume, area):
  return  volume / area 
  

main()
