from django.urls import path
from .views import FinanciamentoImovelListCreateView

urlpatterns = [
    path('financiamento_imovel/', FinanciamentoImovelListCreateView.as_view()),
]