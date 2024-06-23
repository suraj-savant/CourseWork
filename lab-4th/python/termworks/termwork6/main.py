"""
Problem Statement   :
Create an object-oriented program that allows you to enter data for customers and employees.
Problem Details
Create a Person class that provides attributes for first name, last name, and email address.
This class should provide a property or method that returns the person’s fullname.
Create a Customer class that inherits the Person class. This class should add an attribute for
a customer number.
Create an Employee class that inherits the Person class. This class should add anattribute for
a PAN number.
The program should create a Customer or Employee object from the data entered bythe user,
and it should use this object to display the data to the user.
To do that, the program can use the isinstance() function to check whether an object is a
Customer or Employee object.
"""



"""
Person class parent class for the emplyoee and customer

"""
class Person :
    def __init__(self, fname, lname, email) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        pass

    def printPerson(self) :
        print(f"Name : {self.fname} {self.lname}\nEmail : {self.email}")
   
"""
Customer class to store customer details child class of Person
"""

class Customer(Person) :
    def __init__(self, fname, lname, email, custemer_id) -> None:
        super().__init__(fname, lname, email)
        self.customer_id = custemer_id

    def printCustomer(self):
        print("\nCustomer Details : ")
        print("Customer Id :",self.customer_id)
        super().printPerson()


"""
Employee class to store employee details child class of Person
"""

class Employee(Person) :
    def __init__(self, fname, lname, email, pan_number) -> None:
        self.pan_number = pan_number
        super().__init__(fname, lname, email)

    def printEmployee(self):
        print("\nEmployee Details : ")
        super().printPerson()
        print("Pan number :",self.pan_number)




"""
function to display employee or customer based on instance type
"""
def display(obj) :    
    if isinstance(obj, Customer) :
        obj.printCustomer()
        return    
    if isinstance(obj, Employee) :
        obj.printEmployee()
        return



customer = Customer("Suraj", "Savant", "Suraj@gmail", 1)

employee = Employee("Kiran", "Patil", "Kiran@gmail.com", "PAN123")

display(customer)
display(employee)