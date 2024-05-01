from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def pagina_inicial(request):
    return HttpResponse('Pronto para começar a investir!')

def contato(request):
    return HttpResponse('Para dúvidas, entrar em contato pelo e-mail jpsampaio@gmail.com')

def bibliografia(request):
    pessoa = {
        'nome': 'João Paulo',
        'idade': 24,
        'hobby': 'Jogar Futebol'
    }

    return render(request, 'investimentos/bibliografia.html', pessoa)

def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }

    return render(request, 'investimentos/investimento_registrado.html', investimento)