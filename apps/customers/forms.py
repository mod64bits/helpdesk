from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Customer


class CustomerForm(BSModalModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

