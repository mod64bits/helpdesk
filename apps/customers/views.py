from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from .models import Customer
from .forms import CustomerForm


class CustomerListView(ListView):
    model = Customer
    success_message = 'Success: Paciente criado.'
    context_object_name = 'customers'
    template_name = 'customers/list_customer.html'


class CustomerCreateView(BSModalCreateView):
    template_name = 'customers/create_customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customers:customer_list')

    def get_queryset(self):
        return Customer.objects.all().orderby('-created_at')


class CustomerUpdateView(BSModalUpdateView):
    success_url = reverse_lazy('customers:customer_list')
    template_name = 'customers/update_customer.html'
    form_class = CustomerForm
    success_message = 'Success: Cliente Atualizado.'

    def get_queryset(self):
        return Customer.objects.all()

def customers(request):
    data = dict()
    if request.method == 'GET':
        books = Customer.objects.all()
        data['table'] = render_to_string(
            'customers/_customer_table.html',
            {'books': books},
            request=request
        )
        return JsonResponse(data)
