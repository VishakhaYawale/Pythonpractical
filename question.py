a=int(input("Enter first side of triangle:"))
b=int(input("Enter second side of triangle:"))
c=int(input("Enter Third side of triangle:"))

#calculate the semi-perimeter
s=(a+b+c)/2

#calculate the area of triangle
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is  %d0.21' %area)

r=int(input("Enter radius of circle:"))

A=3.14*r*r
print("Area of circle:",A)
