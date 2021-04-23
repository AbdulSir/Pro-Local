from django.urls import path
from django.http import HttpResponse


from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('404/', views.404),
    path('500/', views.500),
]

handler404 = views.404
handler500 = views.500

