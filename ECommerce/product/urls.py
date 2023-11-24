from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    OrderListCreateView,
    OrderRetrieveUpdateDestroyView,
    OrderDetailsListCreateView,
    OrderDetailsRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<str:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<str:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-retrieve-update-destroy'),
    path('order-details/', OrderDetailsListCreateView.as_view(), name='order-details-list-create'),
    path('order-details/<int:pk>/', OrderDetailsRetrieveUpdateDestroyView.as_view(), name='order-details-retrieve-update-destroy'),
]
