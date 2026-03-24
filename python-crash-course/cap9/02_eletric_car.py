from car import Car
from eletric_car import EletricCar

teste_1 = Car("volksvagen", "gol", 2016)
print(teste_1.get_descritive_name())

tesla = EletricCar("tesla", "cybertruck", 2021)
print(tesla.get_descritive_name())
print(tesla.battery_size)
print(tesla.describe_battery())
