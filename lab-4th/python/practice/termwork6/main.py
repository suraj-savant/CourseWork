class Person :
    def __init__(self, first_name, last_name, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_full_name(self) :
        return self.first_name+ " " + self.last_name
    
    def get_email(self) :
        return self.email

class Customer(Person) :
    def __init__(self,cust_no, first_name, last_name, email) -> None:
        super().__init__(first_name, last_name, email)
        self.cust_no = cust_no

    def display_customer(self) :
        print("Customer details are ")
        print(self.cust_no)
        print(super().get_full_name())
        print(super().get_email())

class Employee(Person) :
    def __init__(self,pan_no, first_name, last_name, email) -> None:
        super().__init__(first_name, last_name, email)
        self.pan_no = pan_no

    def display_employee(self) :
        print("Employee details are ")
        print(self.pan_no)
        print(super().get_full_name())
        print(super().get_email())

def display(obj) :
    if isinstance(obj, Customer) :
        obj.display_customer()
    else :
        obj.display_employee()


customer = Customer(10, "Suraj", "Savant", "suraj@gmail.com")
employee = Employee("pan001", "Ravi", "Mishra", "ravi@gmail.com")

display(customer)
print()
display(employee)


    