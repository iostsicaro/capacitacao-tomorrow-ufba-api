from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import SimulacaoEmprestimoSerializer

class SimulacaoEmprestimoCreateView(generics.ListCreateAPIView):
    serializer_class = SimulacaoEmprestimoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            retorno_salvamento = serializer.save()
            
        return Response({
            "data": SimulacaoEmprestimoSerializer(retorno_salvamento, context=self.get_serializer_context()).data,
            "result": "Dados salvos com sucesso!"
        }, status=status.HTTP_201_CREATED)