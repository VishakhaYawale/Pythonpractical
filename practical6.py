h=int(input("Enter your height in centimeters:"))
h=h/2.54
f=h/12
i=h%12
print()
print('Height in feet and inches:{} Feet and {} Inches'.format(round(f),round(i,1)))
