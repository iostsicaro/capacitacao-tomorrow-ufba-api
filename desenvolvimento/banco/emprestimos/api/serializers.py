from rest_framework import serializers
from emprestimos.models import SimulacaoEmprestimo #nosso model

class SimulacaoEmprestimoSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    valor_emprestimo = serializers.DecimalField(max_digits=10, decimal_places=2)
    taxa_juros = serializers.DecimalField(max_digits=5, decimal_places=2)
    prazo_meses = serializers.IntegerField()
    
    class Meta:
        model = SimulacaoEmprestimo
        fields = ['id', 'valor_emprestimo', 'taxa_juros', 'prazo_meses']
        
        def save(self, **kwargs):
            data_send = self.initial_data # dado que vem da requisição
            
            # obter dados oriundos do JSON do self.initial_data recebidos da View(data_send)
            id = data_send['id']
            valor_emprestimo = data_send['valor_emprestimo']
            taxa_juros = data_send['taxa_juros']
            prazo_meses = data_send['prazo_meses']
            
            simulacaoEmpObj = SimulacaoEmprestimo(
                id=id,
                valor_emprestimo=valor_emprestimo,
                taxa_juros=taxa_juros,
                prazo_meses=prazo_meses
            )
            
            simulacaoEmpObj.save()
            
            return simulacaoEmpObj