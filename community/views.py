from re import template
from django.views.generic import TemplateView
from community.models import EnlacesAPI, Community_info, Link_Group


class PortadaView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['comment'] = Community_info.objects.all()
        return context


class LinksGroupView(TemplateView):
    template_name = 'linkgroups.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = Link_Group.objects.all()
        return context
