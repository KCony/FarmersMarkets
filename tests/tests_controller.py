"""Тест для модуля console_controller.py."""

import unittest

from console_controller import *


class TestProcessCommand(unittest.TestCase):
    """Тест для функции process_command."""

    def test_process_command(self):
        """Тест на формирование списка сложной команды (состоящей из трёх элементов)."""
        result_list_command = process_command('list')
        true_list_command = ['list', 'city', 'ASC']
        self.assertEqual(result_list_command, true_list_command)

        result_find_command = process_command('find')
        true_find_command = ['find', 'Troy']
        self.assertEqual(result_find_command, true_find_command)

        result_show_command = process_command('show')
        true_show_command = ['show']
        self.assertEqual(result_show_command, true_show_command)

        result_write_command = process_command('write')
        true_write_command = ['write']
        self.assertEqual(result_write_command, true_write_command)
