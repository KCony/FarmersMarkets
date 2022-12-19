"""Тест для модуля model.py."""

import unittest

from model import *


db_curs = init('test_server.db')[1]


class TestModel(unittest.TestCase):
    """Тест для модуля model.py."""

    def test_init(self):
        """Тест функци init."""
        db_connection, db_cursor = init('test_server.db')
        self.assertTrue(db_connection)
        self.assertTrue(db_cursor)
        close(db_connection, db_cursor)

    def test_list_markets(self):
        """Тест функции list_markets."""
        markets_list = list_markets(db_curs, [])
        true_market_list = ['Caledonia Farmers Market Association - Danville', "18th Street Farmer's Market",
                            "26th Annual Highlands Business Partnership's Farmers Market", "29 Palms Farmers' Market",
                            'Caledonia Farmers Market Association - Danville', "18th Street Farmer's Market",
                            "26th Annual Highlands Business Partnership's Farmers Market", "29 Palms Farmers' Market"]
        self.assertEqual(markets_list, true_market_list)

    def test_list_cities(self):
        """Тест функции all_cities."""
        cities_list = all_cities(db_curs)
        count_cities = len(cities_list)
        true_cities_list = ['Danville', 'Danville', 'Highlands', 'Highlands', 'Scottsbluff', 'Scottsbluff',
                            'Twentynine Palms', 'Twentynine Palms', 'city', 'city']
        self.assertEqual(cities_list, true_cities_list)
        self.assertEqual(count_cities, 10)

    def test_find_market(self):
        """Тест функции find_market."""
        list_id = find_market(db_curs, "18th Street Farmer's Market")
        true_list_id = []
        self.assertEqual(list_id, true_list_id)

    def test_find_by_zip(self):
        """Тест функции find_by_zip."""
        name_market = find_by_zip(db_curs, 5828)
        true_name_market = 'Caledonia Farmers Market Association - Danville'
        self.assertEqual(name_market, true_name_market)

    def test_find_by_city(self):
        """Тест функции find_by_city."""
        list_name_market = find_by_city(db_curs, 'Scottsbluff', 'Nebraska')
        true_list_name_market = ["26th Annual Highlands Business Partnership's Farmers Market"]
        self.assertEqual(list_name_market, true_list_name_market)

    def test_detailed_data(self):
        """Тест функции detailed_data."""
        details_data = detailed_data(db_curs, "18th Street Farmer's Market")
        true_details_data = []
        self.assertEqual(details_data, true_details_data)

