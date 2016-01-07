# Add support for payment

We will use django-oscar-paypal to support payment via paypal
* Add django-oscar-paypal to requirements.txt
* add 'paypal' to INSTALLED_APPS

Create a PayPal sandbox account and 2 test users - a buyer and a seller
* (https://developer.paypal.com/)

Set the seller API credentials in settings
* Change settings into a settings directory, with settings hierarchy
 * modify BASE_DIR
 * modify default settings in wsgi.py and manage.py
* set in override.py:
 * PAYPAL_API_USERNAME = 'test_xxxx.gmail.com'
 * PAYPAL_API_PASSWORD = '123456789'
 * PAYPAL_API_SIGNATURE = '...'

Modify
* urls.py
* settings/base.py

Change checkout button to paypal checkout button
* templates/basket/partials/basket_content.html

That's it, now you can make some purchases using the paypal test buyer
* check out the transactions in dashboard > paypal
* check out the orders in dashboard > fulfilment > orders
