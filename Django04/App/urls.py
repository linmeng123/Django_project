from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cat/$', views.showcat, name='cat'),
    url(r'^home/$', views.home, name='home'),
    url(r'^test1/$', views.test1, name='test1'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),

    url(r'^verifycode/$', views.verifycode, name='verifycode'),
]