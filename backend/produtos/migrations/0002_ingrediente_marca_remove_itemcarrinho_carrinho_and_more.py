# Generated by Django 5.0.6 on 2024-06-18 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produtos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingrediente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="itemcarrinho",
            name="carrinho",
        ),
        migrations.RemoveField(
            model_name="itemcarrinho",
            name="produto",
        ),
        migrations.RemoveField(
            model_name="produto",
            name="categoria",
        ),
        migrations.AddField(
            model_name="categoria",
            name="imagem",
            field=models.ImageField(
                blank=True, null=True, upload_to="categoria_imagem/%Y/%m"
            ),
        ),
        migrations.AddField(
            model_name="categoria",
            name="principal",
            field=models.BooleanField(
                default=False,
                help_text="Define quais categorias iraão aparece na página home",
            ),
        ),
        migrations.AddField(
            model_name="produto",
            name="categorias",
            field=models.ManyToManyField(
                related_name="produtos", to="produtos.categoria"
            ),
        ),
        migrations.AlterField(
            model_name="categoria",
            name="nome",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="produto",
            name="preco",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AddField(
            model_name="produto",
            name="ingredientes",
            field=models.ManyToManyField(to="produtos.ingrediente"),
        ),
        migrations.AddField(
            model_name="produto",
            name="marca",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="produtos.marca",
            ),
        ),
        migrations.DeleteModel(
            name="Carrinho",
        ),
        migrations.DeleteModel(
            name="ItemCarrinho",
        ),
    ]