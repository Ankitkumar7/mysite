from django.conf.urls import url
from django.contrib import admin
from viewscontroller import views
from rest_framework.authtoken  import views as vw

urlpatterns = [
     url(r'^admin/', admin.site.urls),
    url(r'api/users', views.UserCreate.as_view(), name='account-create'),
    url(r'^login/$',view=vw.obtain_auth_token),
]