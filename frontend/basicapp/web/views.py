from django.shortcuts import render
import requests
from django.conf import settings
from django.core.cache import cache
# Create your views here.

def home(request):
    return render(request, 'web/home.html')


def usuarios(request):
    # obtendo os dados da API
    base_url = settings.API_URL
    path = '/employee/'
    print(f'Getting {base_url+path}')
    employee = cache.get('users')
    if not employee:
        response = requests.get(base_url+path)
        employee_data = response.json()
        print('não utilizando cache')
        print(employee_data)
        context = {
            'employees': employee_data,        
        }
        cache.set('users', context, 45)
        print(context)
    else:
        context = employee
        print('utilizando cache')
    return render(request, 'web/usuarios.html', context)

def detalhes(request, usuario_id):
    # obtendo os dados da API
    base_url = settings.API_URL
    path = '/employee/' + str(usuario_id)
    print(f'Getting {base_url+path}')
    details = cache.get(f'details/{usuario_id}')
    if not details:
        print('Não utilizando cache')
        response = requests.get(base_url+path)
        employee_data = response.json()
        context = {
            'employee': employee_data,        
        }
        cache.set(f'details/{usuario_id}', context, 45)
    else:
        print('Utilizando cache')
        context = details
    return render(request, 'web/detalhes.html', context)