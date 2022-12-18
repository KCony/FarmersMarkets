"""Тест для модуля console_ui.py."""

import unittest

from console_ui import *


class TestGetCommandPrompt(unittest.TestCase):
    """Тест для функции get_command_prompt."""

    def test_get_command_prompt(self):
        """Тест для функции get_command_prompt."""
        console = get_command_prompt()
        self.assertEqual(console, 'Input your command => ')
