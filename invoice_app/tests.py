from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, Invoice_Detail


class InvoiceDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            'Date': '2023-09-30T12:00:00Z',
            'Invoice_CustomerName': 'Aditya',
        }
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.url = reverse('invoice_detail', kwargs={'pk': self.invoice.id})  


    def test_retrieve_invoice_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice_details(self):
        updated_data = {
            'Date': '2023-10-01T12:00:00Z',
            'Invoice_CustomerName': 'Updated',
        }
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Invoice_CustomerName'], 'Updated')

    def test_partial_update_invoice_details(self):
        partial_data = {'Invoice_CustomerName': 'Partial Update Customer'}
        response = self.client.patch(self.url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Invoice_CustomerName'], 'Partial Update Customer')

    def test_delete_invoice_details(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Invoice.objects.filter(id=self.invoice.id).exists())

class InvoiceDetailDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice = Invoice.objects.create(Date='2023-09-30T12:00:00Z', Invoice_CustomerName='Aditya')
        self.invoice_detail_data = {
            'invoice': self.invoice,
            'description': 'First Description',
            'quantity': 10,
            'unit_price': 15.99,
            'price': 159.90,
        }
        self.invoice_detail = Invoice_Detail.objects.create(**self.invoice_detail_data)
        self.url = reverse('invoice-detail-detail', kwargs={'pk': self.invoice_detail.id})  


    def test_retrieve_invoice_detail_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice_detail_details(self):
        updated_data = {
            'description': 'Updated',
            'quantity': 20,
            'unit_price': 15.99,  
            'price': 159.90,      
            'invoice': self.invoice.id 
        }
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Updated')
        self.assertEqual(response.data['quantity'], 20)

    def test_partial_update_invoice_detail_details(self):
        partial_data = {'quantity': 15}
        response = self.client.patch(self.url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 15)

    def test_delete_invoice_detail_details(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Invoice_Detail.objects.filter(id=self.invoice_detail.id).exists())
