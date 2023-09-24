from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceList.as_view(), name='invoice_list'),
    path('invoices/<int:pk>/', views.InvoiceDetail.as_view(), name='invoice_detail'),
    path('invoice-details/', views.InvoiceDetailList.as_view(), name='invoice-detail-list'),
    path('invoice-details/<int:pk>/', views.InvoiceDetailDetail.as_view(), name='invoice-detail-detail'),
]