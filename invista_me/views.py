from django.shortcuts import render, redirect, HttpResponse
from .models import Investimentos
from .forms import InvestimentosForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def pagina_inicial(request):
    return HttpResponse('Pronto para começar a investir!')

def contato(request):
    return HttpResponse('Para dúvidas, entrar em contato pelo e-mail jpsampaio@gmail.com')


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

@login_required
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

        
@login_required
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

@login_required
def excluir(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)

    if request.method == 'POST':
        investimento.delete()
        return redirect('lista_investimentos')
        
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})