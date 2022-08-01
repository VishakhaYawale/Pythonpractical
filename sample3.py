class Employee():
    empCount = 0

    def __init__(self, name, salary, dep):
        self.name = name
        self.salary = salary
        self.dept = dep
        Employee.empCount += 1

        def displayEmployee(self):
            print("Name: ", self.name, ",Salary: ", self.salary, ",department:", self.dep)

            name = {}
            salary = {}
            dep = {}
            emp = {}

            for i in range(1, 3):
                print("Enter Your Details for Employee %d " % (i))
                name[i]=input("Enter Your Name for Employee:")
                salary[i]=input("Enter your Salary for Employee:")
                dep[i]=input("Enter Your department for employee:")
                emp[i]=Employee(name[i],salary[i],dep[i])

                print("______________________________")

                for i in range (1,3):
                    emp[i].displayEmployee()

                    print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        pass

