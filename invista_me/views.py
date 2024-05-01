from django.shortcuts import render, redirect, HttpResponse
from .models import Investimentos
from .forms import InvestimentosForm


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

    if request.method == 'POST':
        investimentos_form = InvestimentosForm(request.POST)
        if investimentos_form.is_valid():
            investimentos_form.save()
        return redirect('lista_investimentos')
    else:
        investimentos_form = InvestimentosForm()
        formulario = { 
            'formulario': investimentos_form
        }

        return render(request, 'investimentos/novo_investimento.html', context=formulario)

# def investimento_registrado(request): 
#     investimento = {
#         'tipo_investimento': request.POST.get('TipoInvestimento')
#     }

#     return render(request, 'investimentos/investimento_registrado.html', investimento)


def lista_investimentos(request):
    dados = {
        'dados': Investimentos.objects.all()
    }

    return render(request, 'investimentos/lista_investimentos.html', context=dados)


def detalhes(request, id_investimento):
    dados = {
        'dados': Investimentos.objects.get(pk=id_investimento)
    }

    return render(request, 'investimentos/detalhes.html', dados)


def editar(request, id_investimento):
    investimentos = Investimentos.objects.get(pk=id_investimento)

    if request.method == 'GET':
        formulario = InvestimentosForm(instance=investimentos)

        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    else:
        formulario = InvestimentosForm(request.POST, instance=investimentos)
        if formulario.is_valid():
            formulario.save()
        
        return redirect('lista_investimentos')