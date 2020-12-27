from django.urls import path
from product_portal_api import views

urlpatterns = [
    path('products/', views.ProductLists.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('tokenlogin/', views.tokenlogin),
    path('filterview/', views.FilterView.as_view()),
    path('productview/', views.ProductView.as_view()),
]

