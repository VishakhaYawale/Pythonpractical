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