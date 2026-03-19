import car


class EletricCar(car.Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print("This car has a ", str(self.battery_size), "-kWh battery")


my_tesla = EletricCar("tesla", "model s", 2016)

print(my_tesla.get_descritive_name())
print(my_tesla.describe_battery())
