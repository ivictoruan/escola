from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            # EMAIL EXIGIDO APENAS PARA CADASTRO
            'email': {'write_only':  True, }
        }
        model = Avaliacao
        fields = [  # CAMPOS A SEREM APRESENTADOS NA API
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        ]


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship (1-1)
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinedRelatedField ("RECOMENDADA" )
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail',
    )

    # Primary Key Related Field (MAIS PERFORMÁTICA: envia apenas as Pks)
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
        ]
