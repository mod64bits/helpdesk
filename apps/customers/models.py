from django.db import models
from django.db.models import signals
from apps.core.signals import create_slug
from django.urls import reverse
from apps.core.models import BaseModel
from apps.users.models import User


class Customer(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_to',
        blank=True,
        null=True,
        verbose_name='Usuário',
    )
    fantasy_name = models.CharField('Nome / Nome Fantasia', max_length=100)
    legal_person = models.BooleanField('Pessoa Jurídica', default=False)
    document = models.CharField('CPF/CNPJ', max_length=25)
    phone_number = models.CharField('Telefone', max_length=30, null=True, blank=True)
    is_whatsapp = models.BooleanField('Whatsapp', default=True)
    note = models.TextField('Observação', null=True, blank=True)
    slug_from = 'fantasy_name'

    # def get_absolute_url(self):
    #     return '{}#update'.format(reverse('customers:customer_update', kwargs={'slug': self.slug}))

    def __str__(self):
        return self.fantasy_name

    class Meta:
        abstract = False


class CustomerAddresses(BaseModel):
    address = models.CharField('Endereço', max_length=150)
    district = models.CharField('Bairro', max_length=150)
    initials = models.CharField('Sigla', max_length=2, help_text='Ex: SP')
    number = models.CharField('Numero', max_length=20, null=True, blank=True, help_text='Ex: 58-B')
    reference = models.TextField('Referencia', null=True, blank=True)
    slug_from = 'address'

    def __str__(self):
        return self.address


signals.post_save.connect(create_slug, sender=Customer)

