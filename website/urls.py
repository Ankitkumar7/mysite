from django.conf.urls import url
from django.contrib import admin
from recipes.views import (login_view, logout_view, register_view, index, recipesmain, postRecipe, startTesting, stopTesting, startUatTesting, stopUatTesting)

urlpatterns = [
	url(r'admin/', admin.site.urls),
	url(r'^(?P<request_id>[0-9]+)$', recipesmain, name='recipesmain'),
	url(r'post', postRecipe, name='logout'),
	url(r'register/', register_view, name='register'),
	url(r'login/', login_view, name='login'),
	url(r'logout/', logout_view, name='logout'),
	# url(r'admin/', admin.site.urls),
	url(r'setstatus/', startTesting, name="start" ),
	url(r'deleteStatus/', stopTesting, name="delete"),
	url(r'setuatstatus/', startUatTesting, name="uatstart" ),
	url(r'stopuatesting/', stopUatTesting, name="uatstop"),
    url(r'', index, name='index'),
]
