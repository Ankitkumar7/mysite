"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from viewscontroller import views
urlpatterns = [
 	url(r'^admin/', admin.site.urls),
    url(r'^dayone/', views.dayOneView.as_view()),
    url(r'^daytwo/', views.dayTwoView.as_view()),
    url(r'^daythree/', views.dayThreeView.as_view()),
    url(r'^dayfour/', views.dayFourView.as_view()),
    url(r'^dayfive/', views.dayFiveView.as_view()),
    url(r'^daysix/', views.daySixView.as_view()),
    url(r'^music/', views.music_view.as_view())


]
urlpatterns = format_suffix_patterns(urlpatterns)