"""Uses forex_python module to convert currencies"""

import forex_python.converter
from decimal import Decimal

class Converter:
    def __init__(self):
        self.forex_codes = forex_python.converter.CurrencyCodes()
        self.forex_rates = forex_python.converter.CurrencyRates()

    def validate_currency_code(self, currency_code):
        """ Check if currency code is supported
        >>> c = Converter()
        >>> c.validate_currency_code("USD")
        True
        >>> c.validate_currency_code("XX")
        False
        """
        if self.forex_codes.get_currency_name(currency_code):
            return True
        else:
            return False

    def convert_currency(self, convert_from, convert_to, amount):
        """ Converts amount from one to the other, returns dict of results
        >>> c = Converter()
        >>> c.convert_currency("USD", "USD", 1)
        Decimal('1.00')
        """
        amount = Decimal(amount)
        return round(self.forex_rates.convert(convert_from, convert_to, amount, date_obj=None), 2)

    
        







    