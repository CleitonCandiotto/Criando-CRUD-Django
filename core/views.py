from statistics import mode
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto
from .forms import ProdutoForm


class IndexView(ListView):
    model = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_forms.html'
    fields = ['nome', 'preco']
    sucess_url = reverse_lazy('index.html')