from unittest import TestCase
from helpers import convert_currency

class TestCurrencyConverter(TestCase):
    
    def test_converter(self):
        response = convert_currency("USD", "USD", "1")
        self.assertEqual(response, 1)