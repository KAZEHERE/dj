from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('street/', views.street),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('test/', views.test),
    path('service/', views.service),
    path('fitter/', views.fitter),
    path('amenities/', views.amenities),
    path('errors/', views.errors),
    path('DIREPAIR/', views.DIREPAIR),
    path('CTREET/', views.CTREET),
    path('SERVICE1/', views.SERVICE1),
    path('abonent/', views.abonent),
    path('executor/', views.executor),
    path('nachislsumma/', views.nachislsumm),
    path('paysumma/', views.paysumm),
    path('request/', views.request),
    path('full-width/', views.full),
    path('sidebar/', views.side),
    path('404/', views.four),
    path('price/', views.price),
    path('faq/', views.faq),
    path('pri/', views.pri),
    path('recep/', views.recep),
]