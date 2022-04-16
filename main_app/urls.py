from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('products/', views.ProductList.as_view(), name="products_index"),
    path('products/create/', views.ProductCreate.as_view(), name='products_create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='products_detail'),
    path('products/<int:pk>/update', views.ProductUpdate.as_view(), name='products_update'),
    path('products/<int:pk>/delete', views.ProductDelete.as_view(), name='products_delete'),
]