from django.urls import path
from community.views import PortadaView, ChannelYTView

urlpatterns = [
    path('', PortadaView.as_view(), name='inicio'),
    path('channelYoutube/', ChannelYTView.as_view(), name='channelYoutube'),
]
