from helpers.string import shout
from helpers.math import area

length = 5
width = 8

rectangle_area = area(length, width)
message = f"The area of a {length}-by-{width} rectangle is {rectangle_area}"


print(shout(message))
