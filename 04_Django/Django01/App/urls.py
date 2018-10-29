from django.conf.urls import url

from App import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'^cat/$', views.showcat, name='cat'),

    url(r'^login/$', views.test1, name='login'),
    url(r'^hehe/$', views.test2, name='test2'),
    url(r'^meituan/lalala/$', views.test3, name='test3')
}