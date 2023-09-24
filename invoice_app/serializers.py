from rest_framework import serializers
from .models import Invoice, Invoice_Detail

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        
class Invoice_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_Detail
        fields = '__all__'        