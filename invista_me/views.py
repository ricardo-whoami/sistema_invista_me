from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required
# Adicionado para fazer paginação
from django.core.paginator import Paginator



#def investimentos(request):
    # dados = {
    #     'dados':Investimento.objects.all()
    # }
    # Configurar a paginação============================
def investimentos(request):
    investimentos_list = Investimento.objects.all()
    paginator = Paginator(investimentos_list, 10)  # Divida em 10 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'investimentos/investimentos.html', {'page_obj': page_obj})

    # ==================================================
    # return render(request, 'investimentos/investimentos.html', context=dados,)

def detalhe(request, id_investimento):
    dados = {
        'dados':Investimento.objects.get(pk=id_investimento)
        }
    return render(request, 'investimentos/detalhe.html', dados)

@login_required
def criar(request):
    # Verificando se já existe
    if request.method == 'POST':
        # Salvando os dados informados
        investimento_form = InvestimentoForm(request.POST)
        # Validando os dados
        if investimento_form.is_valid():
            # Se for válido as infos, salvar no db
            investimento_form.save()
        # Redirecinando o usuário para outra página
        return redirect('investimentos')
    else:
        # Se não for um 'POST' um novo formulario será criado/aberto
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario':investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)
    
# Função para editar dados
@login_required
def editar(request, id_investimento):
    # Buscando no db
    investimento = Investimento.objects.get(pk=id_investimento)
    # Verificando qual tipo de requisição -> GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario':formulario})
    # Caso seja do tipo POST
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        # Verificando se o formulário é válido
        if formulario.is_valid():
            # Salvando as infos
            formulario.save()
        return redirect('investimentos')
    
# Função para excluir dados 
@login_required
def excluir(request, id_investimento):
    # Buscando no db
    investimento = Investimento.objects.get(pk=id_investimento)
    # Verificando qual tipo de requisição -> POST
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item':investimento})

# Adicionado para pesquisa ===============================================
#@login_required
def pesquisa(request):
    resultados = None
    if 'q' in request.GET:
        q = request.GET['q']
        resultados = Investimento.objects.filter(investimento__icontains=q)
    return render(request, 'investimentos/pesquisa.html', {'resultados': resultados})