from rest_framework import viewsets
from .serializers import InvoiceSerializer
from .models import Invoice

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.none()

    def get_queryset(self):
        queryset = Invoice.objects.all()
        customer_name = self.request.query_params.get('customer_name', None)
        date = self.request.query_params.get('date', None)

        if customer_name is not None:
            queryset = queryset.filter(customer_name=customer_name)
        if date is not None:
            queryset = queryset.filter(date=date)

        return queryset