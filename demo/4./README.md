# pricing customization

Now, let's simplify things for the shop admin:

* The need to input stock records, choosing partner and sku is cumbersome
  * we usually only have 1 partner
  * sku we can generate automatically
* regarding product price
  * we just want to input the cost price and have the retail price and tax calculated automatically

Let's start with the dashboard

* look at previous step (3)
  * edit a product variant
  * we want just to have a price field available there which will be automatically used as the cost price

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

make some modifications:

* [oscardemo/catalogue/models.py](oscardemo/catalogue/models.py)
* [oscardemo/dashboard/catalogue/forms.py](oscardemo/dashboard/catalogue/forms.py)
* [templates/dashboard/catalogue/product_update.html](templates/dashboard/catalogue/product_update.html)


