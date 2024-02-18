from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Invoice, InvoiceDetail

class InvoiceTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # Create an invoice
        self.invoice = Invoice.objects.create(date='2024-02-18', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description='Test Description', quantity=1, unit_price=100.00, price=100.00)

        self.invoice_data = {
            'date': '2024-02-19', 
            'customer_name': 'New Customer', 
            'invoice_details': [
                {'description': 'New Description', 'quantity': 2, 'unit_price': '200.00', 'price': '400.00'}
            ]
        }

    def test_get_invoices(self):
        url = reverse('invoice-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        url = reverse('invoice-list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        response = self.client.put(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        data = {'customer_name': 'Partially Updated Customer'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
