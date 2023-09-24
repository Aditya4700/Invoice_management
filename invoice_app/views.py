from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics



class InvoiceList(generics.ListCreateAPIView):
    try:
        queryset = Invoice.objects.all()
        serializer_class = InvoiceSerializer
    except Exception as e:
        print("error :", e)    
    
class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    try:
        queryset = Invoice.objects.all()
        serializer_class = InvoiceSerializer    
    except Exception as e:
        print("error :", e)
    
class InvoiceDetailList(generics.ListCreateAPIView):
    try:
        queryset = Invoice_Detail.objects.all()
        serializer_class = Invoice_DetailSerializer
    except Exception as e:
        print("error :", e)
        
class InvoiceDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    try:
        queryset = Invoice_Detail.objects.all()
        serializer_class = Invoice_DetailSerializer    
    except Exception as e:
        print("error :", e)


