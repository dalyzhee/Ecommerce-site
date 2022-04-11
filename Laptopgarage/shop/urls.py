from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.index, name="index"),
    path('product/', views.product, name='product'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('service/', views.service, name='service'),
    path('<category>/', views.category, name='category'),
]