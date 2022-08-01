n=int(input("Enter a number of elements:"))
a=[]
for i in range(0,n):
    elem =int(input("Enter element:"))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in list",round(avg,2))