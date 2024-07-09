from rest_framework import serializers
from financiamentoVeiculo.models import FinanciamentoVeiculo

class FinanciamentoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanciamentoVeiculo
        fields = '__all__'