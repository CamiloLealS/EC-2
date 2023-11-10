from django.shortcuts import render 
from usuario.models import usuario
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

class Home(ListView):
    usuarios = usuario.objects.all()
    template_name = 'proyecto/index.html'
    
    def get_queryset(self):
        return self.usuarios.filter(rol = 'Profesor')

def registro(request):
    return render(request, 'proyecto/registro.html')