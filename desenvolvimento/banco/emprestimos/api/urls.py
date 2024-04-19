from django.urls import path
from .views import SimulacaoEmprestimoCreateView

urlpatterns = [
    path('criar_emprestimo', SimulacaoEmprestimoCreateView.as_view()),
    
]