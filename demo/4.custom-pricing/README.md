# pricing customization

Now, let's simplify things for the shop admin:

* The need to input stock records, choosing partner and sku is cumbersome
  * let's assume we only have 1 partner (ourselves)
  * in that case the sku can be generated automatically
* regarding product price
  * we just want to input the cost price and have the retail price and tax calculated automatically

Let's start with the dashboard -

* we want just to have a cost price and available stock fields available as part of product detail (not in stockrecord)

The dashboard uses html templates, so let's find the product edit template

* [oscar/dashboard/catalogue/product_update.html](https://github.com/django-oscar/django-oscar/blob/1.1.1/src/oscar/templates/oscar/dashboard/catalogue/product_update.html#L97)
  * ok, it's a standard django form, let's find the form
* [oscar/apps/dashboard/catalogue/forms.py](https://github.com/django-oscar/django-oscar/blob/1.1.1/src/oscar/apps/dashboard/catalogue/forms.py#L210)

ok, so we should extend the form to add the price field and num in stock field

```bash
$ ./manage.py oscar_fork_app dashboard.catalogue oscardemo/
$ ./manage.py oscar_fork_app catalogue oscardemo/
```

* add it to settings

make the modifications:

* [oscardemo/catalogue/models.py](oscardemo/catalogue/models.py)
* [oscardemo/dashboard/catalogue/forms.py](oscardemo/dashboard/catalogue/forms.py)
* [templates/dashboard/catalogue/product_update.html](templates/dashboard/catalogue/product_update.html)

ok, now dashboard allows to input only cost price and number of units, but if we look at the product on the site, it doesn't have a price

now comes an interesting part of oscar - the product availability and pricing is managing in strategy objects, this allows great flexibility

for our demo, we need to modify the strategy object to calculate the prcies from the cost price

the oscar partner app manages the strategy, so let's fork it:

```bash
$ ./manage.py oscar_fork_app partner oscardemo/
```

* don't forget to add it to settings..

now, let's see the modifications:

* [oscardemo/partner/strategy.py](oscardemo/partner/strategy.py)
* [oscardemo/partner/prices.py](oscardemo/partner/prices.py)

That's it, simple huh? Now, have a look at the site..
