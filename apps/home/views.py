import datetime
#
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

from apps.entrada.models import Entry
from .models import Home

from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargar los elementos de home
        context["home"] = Home.objects.latest('created')

        # Contexto de portada 
        context["portada"] = Entry.objects.entrada_en_portada()

        # Contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
      
        # Contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()

        # Enviar formulario de suscripcion
        context["suscripcion"] = SuscribersForm

        return context
    
    def post(self, request, *args, **kwargs):
        form = SuscribersForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el formulario
            return redirect(".")  # Redirigir a la misma página
        else:
            # Si el formulario no es válido, recargar la página con errores
            context = self.get_context_data()
            context["suscripcion"] = form
            return self.render_to_response(context)
    


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'

