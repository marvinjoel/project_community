from django.urls import path
from community.views import PortadaView

urlpatterns = [
    path('', PortadaView.as_view(), name='inicio'),
]