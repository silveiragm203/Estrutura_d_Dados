from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# VIEWS -> retornam algo, são funções, request -> response
# View responsável pela tela inicial do médico
def paciente_view(request):
    print('Página Paciente funcionou')
    return HttpResponse('Página inicial do Paciente')
