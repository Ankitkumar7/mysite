from django.conf.urls import url
from django.contrib import admin
from viewscontroller import views
from rest_framework.authtoken  import views as vw
from viewscontroller import views


urlpatterns = [
     url(r'^admin/', admin.site.urls),
    url(r'api/users', views.UserCreate.as_view(), name='account-create'),
    url(r'^login/$',view=vw.obtain_auth_token),
    url(r'^updateuserbalance/(?P<pk>\d+)/$', views.updateUserBalance.as_view()),
    url('^getbalance/(?P<username>.+)/$', views.getUserBalance.as_view()),
    url('^getMobileNumber/(?P<username>.+)/$', views.userMobileNumber.as_view()),
    # url(r'addmobile/$', views.addMobileNumber().as_view, name='addMobile')
     url(r'addmobile', views.CreateMobileNumberView.as_view())

]
