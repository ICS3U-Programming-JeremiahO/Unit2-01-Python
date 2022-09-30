#!/usr/bin/env python3
# Created By: Jeremiah omoike
# Date: September 30, 2022
# This program calculates the Area and perimeter of a circle
import math


def main():
    print(
        "This program calculates the Area and perimeter of a circle for a radius of 5mm."
    )
    radius = 5

    # calculate the circumference (2*pi*r) and area of a circle(pi*r^2)
    circumference = math.pi * 2 * radius
    area = math.pi * radius**2

    # Display the area and circumference of the circle
    print()
    print("The area is: {}mm^2".format(area))
    print("The Circumference is {}mm".format(circumference))


if __name__ == "__main__":
    main()
