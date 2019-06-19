# Exercising to create a function to calculate the area of a cirlce
# This exercise will be continued by a unit test on circle_test.py
# Format of unit test will be name of function

from math import pi

def circle_area(r):
  return pi*(r**2)
  

# Perform a manual interactive test on the above function

# Test Function
radii = [2, 0, -3, 2 + 3j, True, "radius"]
message = "Area of circles with r = {radius} is {area}."

for r in radii:
  A = circle_area(r)
  print(message.format(radius=r, area=A))
