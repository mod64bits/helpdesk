# Generated by Django 4.1 on 2022-08-29 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerAddresses",
            fields=[
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Cadastrado em"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Modificado em"
                    ),
                ),
                ("slug", models.SlugField(editable=False, max_length=255, unique=True)),
                ("address", models.CharField(max_length=150, verbose_name="Endereço")),
                ("district", models.CharField(max_length=150, verbose_name="Bairro")),
                (
                    "initials",
                    models.CharField(
                        help_text="Ex: SP", max_length=2, verbose_name="Sigla"
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True,
                        help_text="Ex: 58-B",
                        max_length=20,
                        null=True,
                        verbose_name="Numero",
                    ),
                ),
                (
                    "reference",
                    models.TextField(blank=True, null=True, verbose_name="Referencia"),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("deleted", models.DateTimeField(editable=False, null=True)),
                (
                    "deleted_by_cascade",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Cadastrado em"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Modificado em"
                    ),
                ),
                ("slug", models.SlugField(editable=False, max_length=255, unique=True)),
                (
                    "fantasy_name",
                    models.CharField(
                        max_length=100, verbose_name="Nome / Nome Fantasia"
                    ),
                ),
                (
                    "legal_person",
                    models.BooleanField(default=False, verbose_name="Pessoa Jurídica"),
                ),
                ("document", models.CharField(max_length=25, verbose_name="CPF/CNPJ")),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "is_whatsapp",
                    models.BooleanField(default=True, verbose_name="Whatsapp"),
                ),
                (
                    "note",
                    models.TextField(blank=True, null=True, verbose_name="Observação"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_to",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
