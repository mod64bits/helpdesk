from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, customers

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('novo/', CustomerCreateView.as_view(), name='customer_create'),
    path('update/<uuid:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/', customers, name='books'),

]
