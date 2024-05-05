from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def novo_usuario(request):
    # Tipo
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        # Validar
        if formulario.is_valid():
            # Salvar
            formulario.save()
            # Informar
            usuario = formulario.cleaned_data.get('username') 
            # Existe outros tipos de messagem, e não somente essa de sucesso 
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!')  

            return redirect('lista_investimentos')
    
    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario': formulario})
