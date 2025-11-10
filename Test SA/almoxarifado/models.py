from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255, unique=True)
    quantidade = models.IntegerField()
    categoria = models.CharField(max_length=255)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
