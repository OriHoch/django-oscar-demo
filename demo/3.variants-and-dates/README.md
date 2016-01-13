# Add variants and dates

Our shop sells lectures and lectures have dates.. So, we should allow each lecture to have multiple dates, and you should be able to buy a ticket for a specific date.

We will use the oscar variants feature, so that each variant is a date of the same lecture. To do that, we need to delete the existing parnet product stock and add variants for each possible date.

Add a "date" product attribute
* dashboard > catalogue > product types > edit product type
* product attributes - add date attribute (not required, because otherwise parent will need it as well)

edit a product and add variants for different dates:
* dashboard > catalogue > products > edit product
* remove existing stock if exists
* add variants + stock for each variant

voila, we have dates

now, let's improve the design a bit

first, let's have a look at the homepage

* http://localhost:8000/

empty.. let's add something to it, as every django app, let's look at urls to see who handles the homepage url

* [oscar/app.py](https://github.com/django-oscar/django-oscar/blob/1.1.1/src/oscar/app.py)
  * oscar uses an [Application](https://github.com/django-oscar/django-oscar/blob/1.1.1/src/oscar/core/application.py) object to handle urls and permissions
  
