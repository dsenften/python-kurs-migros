from decimal import Decimal
from enum import Enum


class Currency(Enum):
    """List of all currencies we support.
    When normalizing currencies, CHF is always used for internal calculations
    """

    CHF = 'CHF'
    EUR = 'EUR'
    USD = 'USD'


class CurrencyHelper:
    """Utilities for currencies"""

    _CURRENCY_DATA = {
        Currency.CHF: {
            'display_name': 'Swiss Franc',
            'numeric_code': 756,
            'default_fraction_digits': 2,
            'sub_unit': 100,
            'convert_to_chf': 1.0,
        },
        Currency.EUR: {
            'display_name': 'Euro',
            'numeric_code': 978,
            'default_fraction_digits': 2,
            'sub_unit': 100,
            'convert_to_chf': 1.11,
        },
        Currency.USD: {
            'display_name': 'US Dollar',
            'numeric_code': 840,
            'default_fraction_digits': 2,
            'sub_unit': 100,
            'convert_to_chf': 0.93,
        },
    }

    @classmethod
    def decimal_precision_for_currency(cls, currency: Currency) -> int:
        """Returns the decimal precision for a currency (number of digits after the decimal)"""
        return cls._CURRENCY_DATA[currency]['default_fraction_digits']

    @classmethod
    def sub_unit_for_currency(cls, currency: Currency) -> int:
        """Returns the sub unit for a currency.
        (eg, the subunit for USD is 100 because there are 100 cents in a dollar)
        """
        return cls._CURRENCY_DATA[currency]['sub_unit']

    @classmethod
    def currency_rate_for(cls, currency: Currency) -> Decimal:
        """Returns the conversion rate for the given currency."""
        return Decimal(cls._CURRENCY_DATA[currency]['convert_to_chf'])
