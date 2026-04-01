import unittest
from city_function import city_country


class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        city_and_country = city_country("união dos palmares", "brasil")
        self.assertEqual(city_and_country, "União Dos Palmares, Brasil")

    def test_city_country_population(self):
        city_country_population = city_country(
            "união dos palmares", "brasil", "60000")
        self.assertEqual(city_country_population,
                         "União Dos Palmares, Brasil, População: 60000")


if __name__ == "__main__":
    unittest.main()
