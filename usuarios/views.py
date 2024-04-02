from django.shortcuts import render, redirect
# Criando formulários para cadastrar usuários
#from django.contrib.auth.forms import UserCreationForm
# ​Link para documentação do UserCreationForm https://docs.djangoproject.com/en/3.2/ref/forms/fields/

# Exibe mensagens para o usuário - Aula 20
from django.contrib import messages
# Adicionado para criação de formulários - Aula 20
# O ponto aponta para a pasta atual
from .forms import UserRegisterForm



def novo_usuario(request):
    # Tratamento de dados: tipo, validar, informar, salvar
    if request.method == 'POST':
        # Criando um formulário
        formulario = UserRegisterForm(request.POST)
        # Verifica se os dados são válidos
        if formulario.is_valid():
            # Salvar no DB
            formulario.save()
            # Informar
            usuario = formulario.cleaned_data.get('username')
            # Podemos exibir outro tipos de mensagens
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html',{'formulario':formulario})