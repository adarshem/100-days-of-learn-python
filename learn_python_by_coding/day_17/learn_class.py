class Car:
    num_of_seats = 0
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def get_age(self):
        # Get the current year from the datetime module
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year
    

car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("Honda", "Civic", 2019)
print(car1.get_info())
print(car2.get_info())
print(car1.get_age())
print(car2.get_age())
car1.num_of_seats += 1
print(car1.num_of_seats)

