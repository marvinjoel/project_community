import json
from os import close
from django.views.generic import TemplateView
from django.shortcuts import render

from community.models import EnlacesAPI, Community_info


class PortadaView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['comment'] = Community_info.objects.all()
        return context


class ChannelYTView(TemplateView):
    template_name = 'channelYoutube.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        with open('community/channels.json', 'r') as f:
            context['channel'] = json.load(f)
            return context
