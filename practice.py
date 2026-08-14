class Employee:

    def __init__(self, Employee_name, Employee_id, Department, Salary):
        self.Employee_name = Employee_name
        self.Employee_id = Employee_id
        self.Department = Department
        self.Salary = Salary

    def Menu(self):
        print("1. Display Details.")
        print("2. Calculate Salary.")
        print("3. Check Salary.")
        print("4. Exit.")


        choice = int(input("Enter your choice :"))

        match choice:
            case 1:
                self.display_details()

            case 2:
                pass

            case 3:
                pass

            case _:
                pass


    def display_details(self):
        print("!!----Employee Details----!!")
        print(" ")
        print("Employee NAME is :",self.Employee_name)
        print("Employee ID is :",self.Employee_id)
        print("Employee's Department is :",self.Department)
        print("Employee's SALARY is :",self.Salary)
        


Employee_name = input("Enter your NAME :")
Employee_id = int(input("Enter your ID :"))
Department = input("Department :")
Salary = float(input("Enter your SALARY :"))

Employee1 = Employee(Employee_name, Employee_id, Department, Salary)

Employee1.Menu()

