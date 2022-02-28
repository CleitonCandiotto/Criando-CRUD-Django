from django.db import models
from django.urls import reverse



class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.nome
