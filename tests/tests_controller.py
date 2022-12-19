"""Тест для модуля console_controller.py."""

import unittest

from console_controller import *


class TesConsoleController(unittest.TestCase):
    """Тест для модуля model.py."""

    def test_distance(self):
        """Тест функции name_by_city."""
        distance_from_degree = distance(10, 43, 23, 5)
        true_distance_from_degree = 2524.9722
        self.assertEqual(round(distance_from_degree, 4), true_distance_from_degree)

    def test_process_command(self):
        """Тест на формирование списка сложной команды (состоящей из трёх элементов)."""
        result_list_command = process_command('list')
        true_list_command = ['list', 'city', 'ASC']
        self.assertEqual(result_list_command, true_list_command)

        result_show_command = process_command('show')
        true_show_command = ['show']
        self.assertEqual(result_show_command, true_show_command)

        result_write_command = process_command('write')
        true_write_command = ['write']
        self.assertEqual(result_write_command, true_write_command)

        result_write_command = process_command('details')
        true_write_command = ['details']
        self.assertEqual(result_write_command, true_write_command)
