class Calculator:
    def addition(self):
        print(a+b)

        def subtraction(self):
            print(a-b)

            def multiplication(self):
                print(a*b)

                def division(self):
                    print(a/b)

                    a=int(input("Enter a first number:"))
                    b=int(input("Enter second number:"))

                    obj =calculator()

                    choice=1
                    while choice !=0:

                        print("1.ADDITION")
                        print("1.SUBTRACTION")
                        print("1.MULTIPLICATON")
                        print("1.DIVISION")

                        choice=int(input("Enter your choice:"))

                        if choice == 1:
                            print(addition())
                        elif choice == 2:
                            print(obj.subtracton())
                        elif choice == 3:
                            print(obj.multiplication())
                        elif choice == 4:
                            print(obj.division())
                        else:
                            print("Invalid choice")

