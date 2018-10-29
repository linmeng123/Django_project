from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^adddog/$',views.adddog),
    url(r'^showdog/$',views.showdog),
    url(r'^addperson/$',views.addperson),
    url(r'^addcard/$',views.addcard),
    url(r'^delperson/$',views.delperson),
    url(r'^getpersoncard/$',views.getpersoncard),
    url(r'^getcardperson/$',views.getpersoncard),
    url(r'^addgrade/$',views.addgrade),
    url(r'addstudent/$',views.addstudent),
    url(r'showgrade/$',views.showgrade),
    url(r'showstudent/$',views.showstudent),
    url(r'^adduser/$', views.adduser),
    url(r'^addgoods/$', views.addgoods),
    url(r'^addcart/$',views.addcart),
    url(r'^showcart/$',views.showcart),
    url(r'^addcollect/$',views.addcollect),
    url(r'^showgoods/$',views.showgoods)
]