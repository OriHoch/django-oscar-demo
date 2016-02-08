# payment (using django-oscar-paypal) and template customization

<p dir=ltr><-- <a href="/demo/1.initial-setup/README.md">Initial Setup</a></p>
<p dir=rtl> <-- <a href="/demo/3.variants-and-dates/README.md">variants, extending core classes, modifying css using less</a></p>

We will use django-oscar-paypal for very easy support of payment via paypal
* Add django-oscar-paypal to [requirements.txt](requirements.txt)
* add 'paypal' to [INSTALLED_APPS](oscardemo/settings/base.py)

Create a PayPal sandbox account and 2 test users - a buyer and a seller
* https://developer.paypal.com/

Set the seller API credentials in settings
* Change settings into a [settings directory](oscardemo/settings), with settings hierarchy
  * modify BASE_DIR
  * modify default settings in [wsgi.py](oscardemo/wsgi.py) and [manage.py](manage.py)
* set in [override.py](oscardemo/settings/override.py.dist):
  * PAYPAL_API_USERNAME = 'test_xxxx.gmail.com'
  * PAYPAL_API_PASSWORD = '123456789'
  * PAYPAL_API_SIGNATURE = '...'

Modify
* [urls.py](oscardemo/urls.py)
* [settings/base.py](oscardemo/settings/base.py)
  * Notice how we add a menu item to the oscar dashboard

Change checkout button to paypal checkout button
* Oscar uses the [Django Extending Templates](https://code.djangoproject.com/wiki/ExtendingTemplates) trick
* It allows to easily extend the core oscar templates and modify specific blocks
* In this example, we want to replace the checkout button which is in the basket_content template
  * First, we look for the relevant template in the core oscar code
    * [oscar/templates/basket/partials/basket_content.html](https://github.com/django-oscar/django-oscar/blob/1.1.1/src/oscar/templates/oscar/basket/partials/basket_content.html#L146)
  * figure out which block we want to modify, in this case - formactions
  * add the template to our code-base (but without oscar prefix)
    * [templates/basket/partials/basket_content.html](templates/basket/partials/basket_content.html)
    * notice that we extend the core oscar template, and only modify the relevant block
    * in this case we replace it completely, but it's also possible to add before or after the existing content - using super

That's it, now you can make some purchases using the paypal test buyer
* check out the transactions in dashboard > paypal
* check out the orders in dashboard > fulfilment > orders

<p dir=ltr><-- <a href="/demo/1.initial-setup/README.md">Initial Setup</a></p>
<p dir=rtl> <-- <a href="/demo/3.variants-and-dates/README.md">variants, extending core classes, modifying css using less</a></p>
