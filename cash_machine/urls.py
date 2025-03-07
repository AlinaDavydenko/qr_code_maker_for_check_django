from django.urls import path
from cash_machine.apps import CashMachineConfig
# from cash_machine.views import CashMachineList
from . import views
from cash_machine.views import generate_receipt

app_name = CashMachineConfig.name

urlpatterns = [
    path('cash_machine/', generate_receipt, name='generate_receipt'),  # CashMachineList.as_view()
]
