from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
    API versão 1 (ap1/v1/)
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        # print(self.queryset)
        if self.kwargs.get('curso_pk'):  # se tiver "curso_pk" na URI
            # avaliacoes relacionadas ao curso
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        else:
            return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(  # RETORNA AVALIAÇÃO (SE HOUVER) DE UM CURSO
                self.get_queryset(),
                curso_id=self.kwargs.get('curso_pk'),
                pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
    API versão 2 (ap1/v2/...)
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    # lookup_field = 'id'

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2
        # curso = self.get_object()
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None: # faz paginação
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data) 

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

