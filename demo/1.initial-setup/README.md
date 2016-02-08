# Initial Django-Oscar Application Setup

If you want, you can skip this and read [django-oscar getting started documentation](http://django-oscar.readthedocs.org/en/latest/internals/getting_started.html) instead..

```bash
# libjpeg-dev is required for Pillow
$ sudo apt-get install libjpeg-dev
# create and activate virtualenv (using virtualenvwrapper)
$ mkvirtualenv oscardemo
$ workon oscardemo
```

* install [requirements](requirements.txt)

```bash
(oscardemo)$ pip install -r requirements.txt
```

* create the [django project](oscardemo)

```bash
(oscardemo)$ django-admin startproject oscardemo .
(oscardemo)$ mkdir media
```

* Modify:
  * [settings.py](oscardemo/settings.py)
  * [urls.py](oscardemo/urls.py)

```bash
(oscardemo)$ ./manage.py migrate
(oscardemo)$ ./manage.py runserver
```

* populate countries (this is required for shipping), using pycountry package

```bash
(oscardemo)$ ./manage.py oscar_populate_countries
```

* create a super user and runserver

```bash
(oscardemo)$ ./manage.py createsuperuser
(oscardemo)$ ./manage.py runserver
```

* Configure the catalogue
  * For our demo app we will use oscar to manage meetups
  * Each product will be a lecture
  * The fulfilment partner will be a meetup promoter which sells tickets for the lecture
  * [/dashboard](http://localhost:8000/dashboard)
    * Fulfilment > Partners > Create
    * Catalogue > Product Types > Create
    * Catalogue > Categories > Create
    * (in a real setup - this will probably be done in a data migration)
* Add some products
  * Catalogue > Products > Add

it works
* [http://localhost:8000/](http://localhost:8000/)
