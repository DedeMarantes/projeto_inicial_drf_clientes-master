from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf":"CPF não é válido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome":"Nome so pode conter letras"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg":"RG deve conter 9 digitos"})   
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular":"numero celular deve seguir o padrao xx xxxxx-xxxx"})          
        return data
    