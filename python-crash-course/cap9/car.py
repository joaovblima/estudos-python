class Car:
    """
    Uma alternativa simples de representar um carro
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descritive_name(self):
        long_name = f"{str(self.year)}, {self.make},  {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Esse carro tem {self.odometer} milhas nele.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("Você não pode reverter um velocímetro")

    def increment_odometer(self, milieage):
        self.odometer += milieage


my_new_car = Car("audi", "a4", 1999)
print(my_new_car.get_descritive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(19)
my_new_car.increment_odometer(55)
my_new_car.read_odometer()
