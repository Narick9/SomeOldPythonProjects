
import unittest

from city_functions import get_formatted_city_title


class CityTestCase(unittest.TestCase):
    """Тесты для city_functions.get_formatted_city_title"""

    def test_city_country(self):
        """"Работают ли такие названия, как 'Santiago, Chile'?"""
        formatted_title = get_formatted_city_title("santiago", "chile")
        self.assertEqual(formatted_title, "Santiago, Chile")


unittest.main()
