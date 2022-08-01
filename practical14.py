n=int(input("Enter a no:"))
f=1
print()
for i in range(1,n+1):
    f=f*i
    print("Factorial of{} is {}".format(str(n),str(f)))

    print()

print("Multipication tabels are:")
for n in range(1,6):
    for i in range(1,10+1):
      m=n*i
      print("{}*{}={}".format(n,i,m))
      print("")