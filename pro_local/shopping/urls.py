from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('about/', views.about, name='about'),
]