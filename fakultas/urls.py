from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persegi/', views.persegi, name='persegi'),
    path('feb/', views.persegipanjang, name='persegipanjang'),
    path('fisip/', views.jajargenjang, name='jajargenjang'),
    path('fh/', views.segitiga, name='segitiga'),
    path('fk/', views.lingkaran, name='lingkaran'),
]