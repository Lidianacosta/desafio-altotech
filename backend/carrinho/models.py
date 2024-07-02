from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.manager import Manager

from produtos.models import Produto

user_model = get_user_model()


# Create your models here.

class ManagerCarrinho(Manager):

    def get_or_create(self, user):
        qs_carrinho = self.get_queryset().filter(user=user, ativado=True)
        if qs_carrinho.exists():
            return qs_carrinho.first()
        return Carrinho.objects.create(user=user)


class Carrinho(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, null=True)
    ativado = models.BooleanField(default=True)

    objects = ManagerCarrinho()

    def __str__(self):
        return f"Carrinho do usuario: {self.user.nome_completo}"


class ItemProduto(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens', null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='carrinho_itens')
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Item: {self.produto}, está no {self.carrinho}"
    
    def total(self):
        return self.produto.preco * self.quantidade