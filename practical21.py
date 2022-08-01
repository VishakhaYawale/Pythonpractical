"""
class Cylinder:
    def __init__(self, r, h):
        self.R = r
        self.H = h

    # end of constructor

    def volume(self):
        V = 3.14 * (self.R ** 2) * self.H
        print("Volume is", V)

        # end of volume

        def surfacearea(self):
            S = 2 * (3.14 * (self.R ** 2) + (2 * 3.14 * self.R) * self.H)
            print("Surface area is", S)

            # end of surfacearea
            # end of class

            class OpenCylinder(Cylinder):
                def surfacearea(self):
                    S = (3.14 * (self.R ** 2) + (2 * 3.14 * self.R) * self.H)
                    print("Surface area of opencyliner is", S)
                    # end of surfacearea
                    # end of class

                    # __main__
                    a = Cylinder(4, 5)
                    a.volume()
                    a.surfacearea()

                    b = OpenCylinder(4, 5)
                    b.volume()
                    b.surfacearea()
"""

class Person:
    def __init__(self,n,a):
        self.N=n
        self.A=a
        #end of constructor

        def showdata(self):
            print("\n Name=",self.N)
            print("Age=",self.A,"yrs")
            #end of showdata
            #end of class constructor

            class Citizen(Person):
                def __init__(self,n,a,nat):
                    Person.__init__(self,n,a)
                    self.Nat=nat
                    #end of constructor

                    def showdata(self):
                        Person.showdata(self)
                        print("Nationality=",self.NAT)
                        #end of showdata

                        class Employee(Citizen):
                            def __init__(self,n,a,nat,eno,j):
                                Citizen.__init__(self,n,a,nat)
                                self.ENO=eno
                                self.J=j
                                #end of constructor

                                def showdata(self):
                                    Citizen.showdata(self)
                                    print("Empno=",self.eno)
                                    print("Job=",self.j)
                                    #end of showdata
                                    #end of class Employee

                                    #__main__

                                    a=Person("Jack",10)
                                    a.showdata()

                                    c=Employee("WILLIAM",30,"BRITTISH",1020,"MANAGER")
                                    c.showdata()


