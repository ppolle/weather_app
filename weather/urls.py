from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index,name = 'index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_user/$',views.login_user,name='login_user'),
]