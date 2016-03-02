"""mantisReports URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from reports.views import proves1, incidencies2015, categories, genera_pdf, incidencies2015_csv

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^proves1/',proves1),
    url(r'^incidencies2015/',incidencies2015),
    url(r'^incidencies2015_csv/',incidencies2015_csv),
    url(r'^categories/',categories),
    url(r'^genera_pdf/',genera_pdf),

]
