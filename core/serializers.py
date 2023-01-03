from rest_framework import serializers
from core.models import User, Itens, Solicitacao


class AddUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'nome_full', 'password')

    def create(self, validated_data, instance=None):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.nome_full = validated_data.get(
            'nome_full', instance.nome_full)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class AddSolicitacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitacao
        fields = (
            'solicitacao_itens',
            'nome',
            'nif',
            'observacao'
        )
    
    def validate(self, attrs):
        EXPECTED_DIGITS = 9

        if not attrs['nif'].isdigit() or len(attrs['nif']) != EXPECTED_DIGITS: 
            raise serializers.ValidationError({"NIF":"Invalido"})

        soma = sum([int(dig) * (EXPECTED_DIGITS - pos) for pos, dig in enumerate(attrs['nif'])])
        resto = soma % 11

        if (attrs['nif'][-1] == '0' and resto == 1):
            resto = (soma + 10) % 11

        # return resto == 0

        return super().validate(attrs)


    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=1)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class SolicitacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitacao
        fields = '__all__'

