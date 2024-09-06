from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Entry, Category

class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 10

    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        return context
    

    def get_queryset(self):
        kw = self.request.GET.get('kword', '')
        categoria = self.request.GET.get('categoria', '')
        # Consulta de entradas
        result = Entry.objects.buscar_entrada(kw, categoria)

        return result



class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"
    context_object_name = 'entrada'


