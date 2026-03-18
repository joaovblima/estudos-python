class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title(), "é um(a)", self.cusine_type)

    def open_restaurant(self):
        print(
            "o",
            self.restaurant_name,
            "esta aberto",
        )


o_barbacoa = Restaurant("Barbacoa", "churrascaria brasileira")
o_mao_de_onca = Restaurant("O mao de onca", "churrascaria brasileira")
casa_do_gorumet = Restaurant("casa do gourmet", "restaurante regional")


o_barbacoa.describe_restaurant()
o_mao_de_onca.describe_restaurant()
casa_do_gorumet.describe_restaurant()
o_barbacoa.open_restaurant()
