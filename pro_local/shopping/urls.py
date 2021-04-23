from django.urls import path

from . import views

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
]