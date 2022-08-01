l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
n=int(input("Enter the number to be divided by:"))
print()
print("The numbers divisible by {} between {} to {} are:".format(n,1,u))
for i in range(1,u+1):
    if(i % n==0):
        print(i,end=" ")