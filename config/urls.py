from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cash_machine.urls', namespace='cash_machine'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
