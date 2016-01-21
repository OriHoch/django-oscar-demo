from oscar.apps.partner.strategy import (
    Selector as OscarSelector,
    UseFirstStockRecord,
    StockRequired,
    Structured
)
from prices import CostBasedPrice
from oscar.apps.partner.prices import Unavailable as PriceUnavailable


# the selector class allows to change the pricing/availability strategy
class Selector(OscarSelector):

    def strategy(self, request=None, user=None, **kwargs):
        # here we can change the strategy based on request/user etc..
        # but for now we will use the same strategy for all cases
        return OscarDemoStrategy(request)


# the strategy object usese multiple classes, each providing some of the functionality
class OscarDemoStrategy(
    UseFirstStockRecord,  # oscar allows multiple stockrecords for the same product
                          # this allows, for example, to have orders of a large quantity be made via a different supplier
                          # but for most cases, we just use the first stock record
    StockRequired,  # this is the basic availability policy strategy
                    # it ensures there is enough stock to allow purchasing the product
                    # also, in case of parent products - if no variants are available, the parent will not be available
    Structured,  # this is the main standard strategy class, providing a lot of common functionality
                 # let's have a look at it: https://github.com/django-oscar/django-oscar/blob/1.1.1/src/oscar/apps/partner/strategy.py#L101
                 # it defines the 2 main functions which any strategy requires -
                 # fetch_for_product and fetch_for_parent (product)
                 # it then returns a PurchaseInfo object containing the price and availability
):

    # here we define the pricing policy based on cost price
    # this will be used for most normal products, see below for parent products
    def pricing_policy(self, product, stockrecord):
        # Check stockrecord has the appropriate data
        if not stockrecord or stockrecord.cost_price is None:
            return PriceUnavailable()
        else:
            # we return our custom price object
            return CostBasedPrice(stockrecord.price_currency, stockrecord.cost_price)

    def parent_pricing_policy(self, product, children_stock):
        stockrecords = [x[1] for x in children_stock if x[1] is not None]
        if not stockrecords:
            return PriceUnavailable()
        else:
            # We take price from first record
            stockrecord = stockrecords[0]
            if stockrecord.cost_price is None:
                return PriceUnavailable()
            else:
                # we return our custom price object
                return CostBasedPrice(stockrecord.price_currency, stockrecord.cost_price)
