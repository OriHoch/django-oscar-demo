from django import forms
from oscar.apps.dashboard.catalogue.forms import (
    ProductForm as OscarProductForm,
    StockRecordFormSet as OscarStockRecordFormSet
)


# here we override the core oscar product form
# and add the cost_price and num_in_stock fields
class ProductForm(OscarProductForm):

    cost_price = forms.FloatField(required=True)
    num_in_stock = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['cost_price'].initial = self.instance.cost_price
        self.fields['num_in_stock'].initial = self.instance.num_in_stock

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit)
        instance.set_stockrecord(self.cleaned_data['cost_price'], self.cleaned_data['num_in_stock'])
        return instance


# we remove the currency and price fields as we will only use the cost_price field
class StockRecordFormSet(OscarStockRecordFormSet):

    def _construct_form(self, i, **kwargs):
        form = super(StockRecordFormSet, self)._construct_form(i, **kwargs)
        del form.fields['price_currency']
        del form.fields['price_excl_tax']
        del form.fields['price_retail']
        return form
