from django.test import TestCase
from django.urls import reverse


class CustomersTest(TestCase):
    def test_customers_url_list(self):
        list_url = reverse('customers:customer_list')
        self.assertEqual(list_url, '/clientes/')

    def test_customers_url_new(self):
        list_url = reverse('customers:customer_create')
        self.assertEqual(list_url, '/clientes/novo/')
