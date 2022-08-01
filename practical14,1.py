number=int(input("Enter number of which user want to print multiplication table:"))

print("The Multilication table of:",number)

for count  in range(1,11):
    print(number,'x',count,"=",number*count)