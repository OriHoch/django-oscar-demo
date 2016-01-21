from oscar.apps.partner.prices import FixedPrice
from decimal import Decimal as D


class CostBasedPrice(FixedPrice):

    def __init__(self, currency, cost_price):
        excl_tax = cost_price * D(2)
        tax = excl_tax * D(.18)
        super(CostBasedPrice, self).__init__(currency, excl_tax, tax)
