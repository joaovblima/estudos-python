class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title(), "é um(a)", self.cusine_type)

    def open_restaurant(self):
        print(
            "o",
            self.restaurant_name,
            "esta aberto",
        )

    def set_number_served(self, clients_served):
        self.number_served = clients_served

    def increment_number_served(self, clients_served):
        self.number_served += clients_served


"""
o_barbacoa = Restaurant("Barbacoa", "churrascaria brasileira")
o_mao_de_onca = Restaurant("O mao de onca", "churrascaria brasileira")
casa_do_gorumet = Restaurant("casa do gourmet", "restaurante regional")


o_barbacoa.describe_restaurant()
o_mao_de_onca.describe_restaurant()
casa_do_gorumet.describe_restaurant()
o_barbacoa.open_restaurant()
print("o restaurante serviu " + str(o_barbacoa.number_served) + " pessoas")
o_barbacoa.set_number_served(24)
print("o restaurante serviu " + str(o_barbacoa.number_served) + " pessoas")
o_barbacoa.increment_number_served(22)
print("o restaurante serviu " + str(o_barbacoa.number_served) + " pessoas")
"""
