from django.urls import path
from .views import FinanciamentoVeiculoListCreateView, FinanciamentoVeiculoDetailView, FinanciamentoVeiculoListView

urlpatterns = [
    path('financiamento_veiculo/', FinanciamentoVeiculoListCreateView.as_view()),
    path('listar_financiamentos/', FinanciamentoVeiculoListView.as_view()),
    path('listar_um_financiamento/<int:pk>/', FinanciamentoVeiculoDetailView.as_view())
]
