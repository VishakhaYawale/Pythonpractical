
lower=int(input("Enter lower range:"))
upper=int(input("Enter upper range:"))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break;
            else:
                print(num)

"""upto =int(input("Find prime number upto:"))

print("\n All Prime numbers upto", upto,"are:")

for num in range(2, upto + 1):
    i = 2
    
    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;
            
            if(i != num):
                print(num, end=" ")"""