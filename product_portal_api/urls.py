# myapi/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from product_portal_api import views

urlpatterns = [
    path('products/', views.ProductLists.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('login/', views.Login.as_view()),
    path('user/', views.User.as_view()),
]

