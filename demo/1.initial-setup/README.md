# Initial Django-Oscar Application Setup

Following mostly follows the django-oscar getting started documentation (http://django-oscar.readthedocs.org/en/latest/internals/getting_started.html)

```
# libjpeg-dev is required for Pillow
$ sudo apt-get install libjpeg-dev
# create and activate virtualenv (using virtualenvwrapper)
$ mkvirtualenv oscardemo
$ workon oscardemo
# install requirements
(oscardemo)$ pip install -r requirements.txt
# create the project (was already done..)
(oscardemo)$ django-admin startproject oscardemo .
(oscardemo)$ mkdir media
```

* see modifications in settings.py
* see modifications in urls.py

```
(oscardemo)$ ./manage.py migrate
(oscardemo)$ ./manage.py runserver
```

* populate countries (this is required for shipping), using pycountry package (in requirements.txt)

```
(oscardemo)$ ./manage.py oscar_populate_countries
```

* create a super user and runserver

```
(oscardemo)$ ./manage.py createsuperuser
(oscardemo)$ ./manage.py runserver
```

* Configure the catalogue
 * For our demo app we will use oscar to manage meetups
 * Each product will be a lecture
 * The fulfilment partner will be a meetup promoter which sells tickets for the lecture
 * http://localhost:8000/dashboard
  * Fulfilment > Partners > Create
  * Catalogue > Product Types > Create
  * Catalogue > Categories > Create
 * (in a real setup - this will probably be done in a data migration)
* Add some products
 * Catalogue > Products > Add

it works
* http://localhost:8000/
