from django.db import models


class Invoice(models.Model):
    Date=models.DateTimeField()
    Invoice_CustomerName=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)
    
class Invoice_Detail(models.Model):
    invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    quantity=models.IntegerField()
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)   
    
    def __str__(self):
        return str(self.id)