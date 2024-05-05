"""
URL configuration for projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista_me import views as invista_me_views
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', invista_me_views.pagina_inicial),
    path('admin/', admin.site.urls),
    path('contato/', invista_me_views.contato, name='contato'),
    path('lista_investimentos/', invista_me_views.lista_investimentos, name='lista_investimentos'),
    path('lista_investimentos/<int:id_investimento>', invista_me_views.detalhes, name='detalhes'),
    path('novo_investimento/', invista_me_views.novo_investimento, name='novo_investimento'),
    path('novo_investimentos/<int:id_investimento>', invista_me_views.editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', invista_me_views.excluir, name='excluir'),
    path('conta/', usuarios_views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]