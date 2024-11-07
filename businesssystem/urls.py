from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('hon/',views.hon,name='hon'),
    path('time/',views.times,name='times'),
    path('weather2/',views.weather2,name='weather2'),
    path('weather1/',views.weather3,name='weather'),
    path('qrcode3/', views.qrocode2, name='qrcode9'),
    path('qrcode/',views.qrcode12,name='qrcode1'),
    path('contactus/',views.contactus1,name='contactus1'),
    path('contactus1/',views.contactus3,name='contactus'),
    path('register/',views.registerpage,name='register2'),
    path('registers/',views.registerpage1,name='register1'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('login1/',views.login1,name='login1'),
    path('adminabout/',views.adminabout),
    path('adminhome/',views.adminhome),
    path('purchase/',views.purchase),
    path('logout/',views.logout,name='logout'),
    path('details/',views.deatils,name='details'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)