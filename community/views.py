from django.views.generic import TemplateView
from community.models import EnlacesAPI, Community_info



class PortadaView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['comment'] = Community_info.objects.all()
        return context