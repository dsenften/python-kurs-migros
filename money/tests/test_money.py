import unittest
from decimal import Decimal

from money.currency import Currency
from money.exceptions import InvalidAmountError
from money.money import Money


class TestMoney(unittest.TestCase):
    """Money tests"""

    def test_construction(self):
        money = Money('3.95')
        assert money.amount == Decimal('3.95')
        assert money.currency == Currency.CHF

        money = Money('1', Currency.USD)
        assert money.amount == Decimal('1')
        assert money.currency == Currency.USD

        with self.assertRaises(InvalidAmountError):
            Money('3.956', Currency.USD)

    def test_convert_to_chf(self):
        money = Money('3.95')
        money = money.convert_to_chf()
        assert money.amount == Decimal('3.95')
        assert money.currency == Currency.CHF

        money = Money(1, Currency.USD)
        money = money.convert_to_chf()
        assert money.currency == Currency.CHF
        assert money.amount == Decimal('0.93')

    def test_add_money(self):
        a = Money('2.50')
        b = Money(1.50)
        result = a + b

        assert result.currency == Currency.CHF
        assert result.amount == Decimal(4.0)

    #
    # def test_add_literal(self):
    #     a = Money('2.50')
    #     result = a + 15.5
    #
    #     assert result.currency == Currency.CHF
    #     assert result.amount == Decimal(18.0)


if __name__ == '__main__':
    unittest.main()
