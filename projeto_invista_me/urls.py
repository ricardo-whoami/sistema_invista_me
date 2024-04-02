
from django.contrib import admin
from django.urls import path
from invista_me import views
from usuarios import views as usuario_views # Views do projeto usuarios
from django.contrib.auth import views as auth_views # Usado para autenticação

# Aqui criamos as rotas/caminho para as páginas HTML
urlpatterns = [
    # Painel do admin
    path('admin/', admin.site.urls),
    # Página do app usuarios
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    # Página inicial
    path('',views.investimentos, name='investimentos'),
    # Página para investimento
    path('novo_investimento/', views.criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', views.excluir, name='excluir'),
    path('/<int:id_investimento>', views.detalhe, name='detalhe'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),# Adicionado 

   
]
