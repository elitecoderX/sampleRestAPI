from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=255)

    class Meta:
        app_label = 'sampleRestAPI'

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_details')
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'sampleRestAPI'
