"""n=int(input("Enter a number of elements:"))
a=[]

for i in range(0,n):
    elem=int(input("Enter a number"))
    a.append(elem)
avg=sum(a)/n
print("Average of numbers is",round(avg,2))"""


"""
x=10
y=20
x=x+y
y=x-y
x=x-y
print("x is :",x,"y is:",y)"""

"""
5th practical
import math

side=20

print("Area of Square is",side*side)
print("Perimeter of Square is",side*4)

radius=5
height=3

print("Perimeter of Cone is", 2*(math.pi)*radius)
print("Volume of cone is",(math.pi)*(radius*radius)*(height/3))  """

"""
6th practical
h=int(input("Enter a height in centimeter:"))
h=h/2.54
f=h/12
i=h%12
print()
print("Height in feet and inches:{}feet{} Inches".format(round(f),round(i,1)))"""

"""
7th practcal
n=int(input("Enter a number:"))
s=0
while(n > 0):
    dig=n%10
    s=s+dig
    n=n//10
print("The total sum of digits 'is:",s)"""

"""
8 th practcal

l=int(input("Enter a lower limit:"))
u=int(input("Enter a upper limit:"))
n=int(input("Enter the number to be divided :"))

print()

for i in range(l,u+1):
    if(i%n==0):
        print(i,end=" ")
"""

"""
Practcal 9

#Creating a list

print("Empty list")
demo_list=[]
print("demo_list:",demo_list)
print()

#Adding element to the list
demo_list.append('Name')
demo_list.append('Number')
demo_list.append('Last Name')
print("After Adding elements to the list:")

print("demo_list:",demo_list)
print()

#Delleting the Eleement form list
del(demo_list[2])
print("After deleting the elements form list:")
print("demo_list:",demo_list)
print()

#sorting the element from list
demo_list.sort()
print("After sorting the elements:")
print("demo_list:",demo_list)
print()

#counting the elements in list
print("Number of elements:",len(demo_list))"""

"""

Practical 10

l1=[78,29,21,43]
l2=[32,2,89,3]
my_list=l1+l2
my_list.sort()
print("l1:",l1)
print()
print("l2:",l2)

print()
print("Merged List:",my_list)"""

"""

Practical 11

a=[10,20,30,10,20,30,40,20,50,60,70]

uniq_items=[]
dup_items=set()

for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

        print(dup_items)
"""

"""
Prctical 12

my_dict={"name":"Karan","Surname":"Patel", "age":32 ,"favourite_dish":"jalebi"}
print(my_dict)

my_dict["fav-personn"]="Ankita"
print(my_dict)

my_dict.pop("age")
print(my_dict)

del my_dict"""

"""
lower=20
upper=40

print("Prime numbers in the range are:")

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
            else:
                print(num)
"""

"""
Practical 13.2

list1=[1,2,3,5,6,8,9,13,16,7,17,20,22,14,15,54]
list_baby=[]
list_school=[]
list_adult=[]

for i in list1:
    if(i <= 6 ):
        list_baby.append(i)
        if(i > 6 and i < 18):
            list_school.append(i)
            if(i > 18 ):
                list_adult.append(i)

                print(len(list1))
                print(len(list_baby))
                print(len(list_school))
                print(len(list_adult)) """
"""

num=int(input("Enter a number:"))
f=1
for i in range(1,num+1):
    f=f*i
    #end of loop

print("factorial of",num,"is",f)

"""

"""

number=int(input("Enter number of which user want to print multiplication table:"))

print("The multiplication table of:",number)

for count in range(1,11):
    print(number,'x',count,"=",number*count) """

"""
def my_mean(m):
    return sum(m) / len(m)

my_mean([4,8,6,7,8,1,3,2,11,5])"""

"""
def my_median(sample):
    n=len(sample)
    index=n // 2 """

"""

if n%2:
    return sorted(sample)[index]

return sum(sorted(sample)[index - 1: index + 1]) / 2
"""

"""
Practcal 16

def print_factors(x):
    print("The factors of ", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


num = 10
print_factors(num)
"""

"""

import math
num=4
list=[1,2]
hello="hello"

try:
    print(num/0)
    print(list[0])
    print(math.sqrt(-2))
    print(hello/1)

except ZeroDivisionError:
    print("Zero division error occur")
except IndexError:
    print("array index out of range")
except TypeError:
    print("type error occured")
except ValueError:
    print("Value error occured")
"""
"""

    f=open("C:\myfile.txt")
    file_data=f.read()
    f.close()

    print(file_data)
except FileNotFoundError:
     print("File Not exists")
    
"""



"""
f = open("first.txt", "wt")
f.write("This is a line")

with open('first.txt', 'a') as f:
    f.write('Hello')
"""

"""
file=open("C:\first.txt","rt")
data=file.read()
words=data.split()

print("Number of words in text file:",len(words))
"""


def addition():
    print(a+b)

    def subtraction(self):
        print(a-b)

        def multiplication(self):
            print(a*b)

            def division(self):
                print(a/b)

                a=int(input("Enter a first number:"))
                b=int(input("Enter b second number:"))

                obj=Calculator()

                choice=1
                while choice !=0:
                    print("1.Addition")
                    print("2.Subtraction")
                    print("3.Multipication")
                    print("4.Division")

                    choice=int(input("Enter your choice:0"))

                    if choice==1:
                        print(obj.addition())
                        if choice ==2:
                            print(obj.subtration())
                            if choice==3:
                                print(obj.multiplication())
                                if choice==4:
                                    print(obj.division())
                                else:
                                    print("Invalid Choice")


class Calculator:
    pass