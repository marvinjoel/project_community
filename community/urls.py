from django.urls import path

from community.views import PortadaView, LinksGroupView

urlpatterns = [
    path('', PortadaView.as_view(), name="home"),
    path('groups', LinksGroupView.as_view(), name="groups")
]
