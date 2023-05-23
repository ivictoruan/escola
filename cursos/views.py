from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers  import CursoSerializer, AvaliacaoSerializer

from cursos.models import Curso, Avaliacao


class CursoAPIView(APIView):
    """
    API DE CURSOS do canal ...
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API DE AVALIAÇÕES do canal ...
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)