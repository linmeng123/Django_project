from django.conf.urls import url

from App import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^datail/(\d+)/(\d+)/(\d+)/$',views.datail,name='datail'),
    url(r'^requesttext/$',views.requesttext,name='requesttext'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^showcookie/$',views.showcookie,name='showcookie'),
    url(r'^jisuanqi/$',views.jisuanqi,name='jisuanqi')

]