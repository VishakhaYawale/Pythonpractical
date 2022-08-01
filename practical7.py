num = int(input("Enter any number:"))
s=0
while num !=0:
    s=s+(num % 10)
    num = num // 10
    print("Sum of Digits in given number is",s)
