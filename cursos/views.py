from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import EhSuperUser

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
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,)

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):  # .../avaliacoes/ <- A FUNÇÃO FORMA ESTA URL!
        self.pagination_class.page_size = 2
        # [BUSCA AVALIAÇÕES] que tem como Primary Key
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        # faz paginação das avaliações
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(
                page, many=True)  # SERIALIZAÇÃO da página
            # RESPONDE com a página serializada
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)  # Responde sem a página


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
