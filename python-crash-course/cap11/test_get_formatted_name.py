import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name("joao", "lima")
        self.assertEqual(formatted_name, "Joao Lima")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("joao", "lima", "victor")
        self.assertEqual(formatted_name, "Joao Victor Lima")


if __name__ == "__main__":
    unittest.main()
