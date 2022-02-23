from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import ServiceProvider
from django.views.generic import DetailView,ListView
from django.forms import models
# Create your views here.
class AddServiceProvider(CreateView):
    model = ServiceProvider
    fields = ['name', 'address', 'email', 'phone', 'website', 'description']
    template_name = 'serviceprovider/add_serviceprovider.html'
    success_url = '/serviceprovider/view'

class Serviceproviderdetail(DetailView):
    model = ServiceProvider
    context_object_name = 'serviceprovider'
    template_name = 'serviceprovider/detail_serviceprovider.html'

class Listserviceprovider(ListView):
    model = ServiceProvider
    serviceproviders = model.objects.all()
    context_object_name = 'serviceproviders'
    template_name = "serviceprovider/list_serviceprovider.html"

class Deleteserviceprovider(DeleteView):
    model = ServiceProvider
    template_name = "serviceprovider/delete_serviceprovider.html"
    success_url = '/serviceprovider/view'

class Updateserviceprovider(UpdateView):
    model = ServiceProvider
    fields = ['name', 'address', 'email', 'phone', 'website', 'description']
    template_name = 'serviceprovider/update_serviceprovider.html'
    success_url = '/serviceprovider/view'

