from oscar.apps.catalogue.abstract_models import AbstractProduct
from oscar.core.loading import get_classes
from django.conf import settings

StockRecord, Partner = get_classes('partner.models', ('StockRecord', 'Partner'))


class Product(AbstractProduct):

    @property
    def cost_price(self):
        # oscar has the prices and stock in a stockrecord model
        # in this case, we just use the first stockrecord, always
        if self.has_stockrecords:
            return self.stockrecords.first().cost_price
        else:
            return 0

    @property
    def num_in_stock(self):
        if self.has_stockrecords:
            return self.stockrecords.first().num_in_stock
        else:
            return 0

    def set_stockrecord(self, cost_price, num_in_stock):
        if self.has_stockrecords:
            stockrecord = self.stockrecords.first()
        else:
            # when creating a new stockrecord, we make some assumptions here:
            # there is only 1 partner
            # for sku we just use the product id with a prefix
            stockrecord = StockRecord.objects.create(
                partner=Partner.objects.first(), product=self, partner_sku='OD-%s'%self.pk, price_currency=settings.OSCAR_DEFAULT_CURRENCY
            )
        stockrecord.cost_price = cost_price
        stockrecord.num_in_stock = num_in_stock
        stockrecord.save()


from oscar.apps.catalogue.models import *  # noqa