from decimal import Decimal, ROUND_HALF_UP

from babel.numbers import format_currency

from money.currency import Currency
from money.currency import CurrencyHelper
from money.exceptions import InvalidAmountError, CurrencyMismatchError, InvalidOperandError


class Money:
    """Class representing a monetary amount"""

    def __init__(self, amount: 0.0, currency: Currency = Currency.CHF) -> None:
        self._amount = Decimal(amount)
        self._currency = currency

        if self._round(self._amount, currency) != Decimal(amount):
            raise InvalidAmountError

    def convert_to_chf(self) -> 'Money':
        """Normalizes (CHF) the current money object """
        amount = self._amount * CurrencyHelper.currency_rate_for(self._currency)
        amount = self._round(amount, Currency.CHF)
        return Money(amount, Currency.CHF)

    @property
    def amount(self) -> Decimal:
        """Returns the numeric amount"""
        return self._amount

    @property
    def currency(self) -> Currency:
        """Returns the currency"""
        return self._currency

    def __add__(self, other: 'Money') -> 'Money':
        """Add two money objects.
        Both must correspond to the same currency. If not, we'll convert
        both sides to CHF.
        """

        if self.currency != other.currency:
            self = self.convert_to_chf()
            other = other.convert_to_chf()

        return self.__class__(str(self.amount + other.amount), self.currency)

    def __radd__(self, other: 'Money') -> 'Money':
        return self.__add__(other)

    def __str__(self):
        """String representation of our Money object"""
        return f'{self._currency.name} {self._amount}'

    def __repr__(self):
        """Representation of our Money object"""
        return f'Money({self.amount}, {self.currency})'

    def format(self, locale: str = 'de_CH') -> str:
        """Returns a string of the currency formatted for the specified locale"""
        return format_currency(self.amount, self.currency.name, locale=locale)

    def _assert_same_currency(self, other: 'Money') -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError

    @staticmethod
    def _round(amount: Decimal, currency: Currency) -> Decimal:
        sub_units = CurrencyHelper.sub_unit_for_currency(currency)
        # rstrip is necessary because quantize treats 1. differently from 1.0
        rounded_to_subunits = amount.quantize(Decimal(str(1 / sub_units).rstrip('0')),
                                              rounding=ROUND_HALF_UP)
        decimal_precision = CurrencyHelper.decimal_precision_for_currency(currency)
        return rounded_to_subunits.quantize( \
            Decimal(str(1 / (10 ** decimal_precision)).rstrip('0')), \
            rounding=ROUND_HALF_UP)
