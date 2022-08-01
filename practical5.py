s=int(input("Enter length of side of square:"))
area=s*s
perimeter=4*s
print("Area of Rectangle:",area)
print("Perimeter of Rectangle:",perimeter)

import math
pi=math.pi

def volume(r,h):
    return(1/3)*pi*r*r*h

def surfacearea(r,s):
    return pi*r*s+pi*r*r

radius=float(5)
height=float(12)
slat_height=float(13)
print("Volume of cone",volume(radius,height))
print("Surface Area of cone:",surfacearea(radius,slat_height))