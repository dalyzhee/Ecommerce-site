from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.index, name="index"),
    path('product/', views.product, name='product'),
    path('service/', views.service, name='service'),
]