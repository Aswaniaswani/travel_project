from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('regindex',views.regindex, name='regindex'),
    path('ruser',views.ruser, name='ruser'),
    path('logindex',views.logindex,name='logindex'),
    path('loginuser',views.loginuser, name='loginuser'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('guide',views.guide,name='quide'),
    path('service',views.service,name='service'),
    path('single',views.single,name='single'),
    path('contact',views.contact,name='contact'),
    path('contactus',views.contactus,name='contactus'),
    path('career',views.career,name='career'),
    path('travelguide',views.travelguide,name='travelguide'),
    path('indexapply',views.indexapply,name='indexapply'),
    path('appnow',views.appnow,name='appnow'),
]