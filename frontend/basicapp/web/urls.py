from django.urls import path
from . import views 


app_name = 'web'
urlpatterns = [ 
        path('', views.home, name='home'), 
        path('usuarios', views.usuarios, name='usuarios'), 
        path('detalhes/<int:usuario_id>', views.detalhes, name='detalhes')
]