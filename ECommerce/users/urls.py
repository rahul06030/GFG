from django.urls import path
from .views import CustomerLoginView, CustomerLogoutView, CustomerRegistrationView

urlpatterns = [
    path('customer/register/', CustomerRegistrationView.as_view(), name='customer-register'),
    path('customer/login/', CustomerLoginView.as_view(), name='customer-login'),
    path('customer/logout/', CustomerLogoutView.as_view(), name='customer-logout'),
]
