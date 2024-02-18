from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id','date', 'customer_name', 'invoice_details']

    def create(self, validated_data):
        invoice_details_data = validated_data.pop('invoice_details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in invoice_details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        invoice_details_data = validated_data.pop('invoice_details', None)
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()

        if invoice_details_data is not None:
            # Get the ids of the existing details
            existing_detail_ids = set(instance.invoice_details.values_list('id', flat=True))

            # Update or create invoice details
            for detail_data in invoice_details_data:
                detail_id = detail_data.get('id')
                if detail_id in existing_detail_ids:
                    # Update existing invoice detail
                    detail = InvoiceDetail.objects.get(id=detail_id)
                    detail.description = detail_data.get('description', detail.description)
                    detail.quantity = detail_data.get('quantity', detail.quantity)
                    detail.unit_price = detail_data.get('unit_price', detail.unit_price)
                    detail.price = detail_data.get('price', detail.price)
                    detail.save()
                    existing_detail_ids.remove(detail_id)
                else:
                    # Create new invoice detail
                    InvoiceDetail.objects.create(invoice=instance, **detail_data)

            # Delete any remaining details
            if existing_detail_ids:
                InvoiceDetail.objects.filter(id__in=existing_detail_ids).delete()

        return instance
