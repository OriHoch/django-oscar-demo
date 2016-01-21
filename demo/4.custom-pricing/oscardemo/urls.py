"""oscardemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static
from paypal.express.dashboard.app import application as paypal_application


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # django admin is not officially supported by oscar - you should use the dashboard instead
    url(r'^admin/', include(admin.site.urls)),

    # paypal
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    url(r'^dashboard/paypal/express/', include(paypal_application.urls)),

    url(r'', include(application.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

