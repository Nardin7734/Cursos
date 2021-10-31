from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_e_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'Número de CPF inválido!'})
        if not nome_e_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Não inclua números neste campo.'})
        if not rg_e_valido(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve possuir nove dígitos'})
        if not celular_e_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O número de celular deve seguir o seguinte padrão: XX '
                                                          'XXXXX-XXXX'})
        return data
