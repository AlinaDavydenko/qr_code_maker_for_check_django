from cash_machine.utils import make_qr_code
import pdfkit

import os

from django.shortcuts import render
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from .models import Item
from .serializers import CashMachineRequestSerializer
from django.template.loader import render_to_string
import datetime
from rest_framework.permissions import AllowAny

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')


@api_view(['POST'])
@permission_classes([AllowAny])
def generate_receipt(request):
    serializer = CashMachineRequestSerializer(data=request.data)
    if serializer.is_valid():
        items_ids = serializer.validated_data['items']
        items = Item.objects.filter(id__in=items_ids)

        total_sum = 0
        item_details = []

        for item in items:
            total_sum += item.price
            item_details.append({
                'title': item.title,
                'quantity': 1,  # по умолчанию считаем количество как 1
                'price': item.price
            })

        current_time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')

        context = {
            'items': item_details,
            'total_sum': total_sum,
            'date': current_time  # Можно использовать текущую дату, например, через datetime
        }

        html_check = render_to_string('cash_machine/item_list.html', context)

        pdf_path = os.path.join('media', 'pdf_files', 'example.pdf')  # путь сохранения pdf

        pdfkit.from_string(html_check, pdf_path, configuration=config)

        qr_code_path = os.path.join('media', 'qr_codes', 'receipt_qr.png')

        # формирование qr_coda
        qr_code_maker = make_qr_code(pdf_path, qr_code_path)
        print(qr_code_maker)

        return render(request, 'cash_machine/item_list.html', context)
