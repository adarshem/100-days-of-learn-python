class Employee:
    company_name = "TechCorp"

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name  # Modify class attribute


my_employee1 = Employee()
my_employee2 = Employee()

print(my_employee1.company_name)  # Output: TechCorp
print(my_employee2.company_name)  # Output: TechCorp

Employee.change_company_name("TechCorp Inc.")

print(my_employee1.company_name)  # Output: test tech.
print(my_employee2.company_name)  # Output: TechCorp Inc.



class BankAccount:
    interest_rate = 0.03  # Class attribute (3% interest)

    def __init__(self, balance):
        self.balance = balance

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate  # Modifies class attribute

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0  # Utility method for validation

# Set interest rate for all accounts
BankAccount.set_interest_rate(0.05)
print(BankAccount.interest_rate)  # 0.05

# Validate deposit amount
print(BankAccount.is_valid_amount(500))  # True
print(BankAccount.is_valid_amount(-20))  # False


# Try inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"{self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, modal, num_doors):
        super().__init__(make, modal)
        self.num_doors = num_doors


car1 = Car("Toyota", "Corolla", 4)
car1.display_info()  # Output: Toyota Corolla


