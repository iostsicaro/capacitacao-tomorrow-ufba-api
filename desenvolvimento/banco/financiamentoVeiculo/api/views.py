from rest_framework import generics
from rest_framework.response import Response
from .serializers import FinanciamentoVeiculoSerializer
from financiamentoVeiculo.models import FinanciamentoVeiculo

class FinanciamentoVeiculoListCreateView(generics.ListCreateAPIView):
    queryset = FinanciamentoVeiculo.objects.all()
    serializer_class = FinanciamentoVeiculoSerializer
    
class FinanciamentoVeiculoDetailView(generics.RetrieveAPIView):
    queryset = FinanciamentoVeiculo.objects.all()
    serializer_class = FinanciamentoVeiculoSerializer
    
class FinanciamentoVeiculoListView(generics.ListAPIView):
    queryset = FinanciamentoVeiculo.objects.all()
    serializer_class = FinanciamentoVeiculoSerializer    