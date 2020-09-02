# from forex_python.converter import CurrencyCodes, CurrencyRates, Common, RatesNotAvailableError, DecimalFloatMismatchError
import forex_python.converter

class Converter:
    def __init__(self):
        self.forex_codes = forex_python.converter.CurrencyCodes()
        self.forex_rates = forex_python.converter.CurrencyRates()

    def validate_currency_code(self, currency_code):
        """ Check if currency code is supported """
        if forex_codes.get_currency_name(currency_code):
            return True
        else:
            return False

    def convert_currency(self, convert_from, convert_to, amount):
        """ Converts amount from one to the other, returns dict of results """
        converted_amt = self.forex_rates.convert(convert_from, convert_to, amount, date_obj=None)
        return {"convert_from": convert_from, "convert_to": convert_to, "starting_amount": amount, "converted_amount": converted_amt}
        







    