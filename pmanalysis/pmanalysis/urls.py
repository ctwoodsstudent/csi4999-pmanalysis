"""pmanalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from signup import views
#from signup.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.landing, name='landing'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^about/$', views.about, name='about'),
    url(r'^creators/$', views.creators, name='creators'),
    url(r'^geo/$', views.geo, name='geo'),
    #path('geo/', views.GeoDataView.as_view(), name='geo'),
    url(r'^search/$', views.search, name='search'),
    url(r'^results/$', views.results, name='results'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^logged_out/$', views.logout, name='logged_out'),
    url(r'^analysis/$', views.analysis, name='analysis'),
    url(r'^analysis/itemsInFolder/$', views.itemsInFolder, name='selectItem'),
    url(r'^analysis/runTest/$', views.runTest, name='runTest'),
    url(r'^analysis/deleteFolder/$', views.deleteFolder, name='runTest'),
    url(r'^geo/itemsInGeo/$', views.itemsInGeo, name='selectItem'),
    url(r'^geo/runTestGeo/$', views.runTestGeo, name='runTest')




]
