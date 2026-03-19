import restaurant


class IceCreamStand(restaurant.Restaurant):
    def __init__(self, restaurant_name, cusine_type, flavors):
        super().__init__(restaurant_name, cusine_type)
        self.flavors = flavors

    def get_flavors(self):
        for flavor in self.flavors:
            print(flavor)


frutilla = IceCreamStand(
    "frutilla", "sorveteria", ["morango", "napolitano", "chocolate"]
)
frutilla.get_flavors()
frutilla.describe_restaurant()
