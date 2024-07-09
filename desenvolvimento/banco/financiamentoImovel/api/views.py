from rest_framework import generics
from rest_framework.response import Response
from .serializers import FinanciamentoImovelSerializer
from financiamentoImovel.models import FinanciamentoImovel

class FinanciamentoImovelListCreateView(generics.ListCreateAPIView):
    queryset = FinanciamentoImovel.objects.all()
    serializer_class = FinanciamentoImovelSerializer