from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import User, Itens, Solicitacao
from core.serializers import UserSerializer, AddUserSerializer, AddSolicitacaoSerializer, SolicitacaoSerializer
from core.query_sql import conexao
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import render


class UserView(APIView):
    def edit(self, request, pk, partial=False):
        if pk:
            self.check_pk_none(pk)
            user = User.objects.get(pk=pk)
            data, status_ = self.edit_serializer(
                request, user, partial=partial)

        usuario = request.user
        data, status_ = self.edit_serializer(request, usuario, partial=partial)

        return data, status_

    def edit_serializer(self, request, user, partial=False):
        serializer = AddUserSerializer(
            user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        status_ = status.HTTP_200_OK

        return data, status_

    def check_pk_none(self, pk):
        usuario = User.objects.filter(pk=pk)

        if len(usuario) == 0:

            msg = f'Usuario com id {pk} não encontrado'
            status_ = status.HTTP_404_NOT_FOUND
            return Response({"error": msg}, status=status_)

        return False

    def get(self, request, pk=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AddUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        data, status_ = self.edit(request, pk)
        return Response(data, status=status_)

    def patch(self, request, pk, format=None):
        data, status_ = self.edit(request, pk, partial=True)
        return Response(data, status=status_)


class SolicitacaoView(APIView):
    renderer_classes = (TemplateHTMLRenderer,)

    def edit(self, request, pk, partial=False):
        if pk:
            self.check_pk_none(pk)
            user = User.objects.get(pk=pk)
            data, status_ = self.edit_serializer(
                request, user, partial=partial)

        usuario = request.user
        data, status_ = self.edit_serializer(request, usuario, partial=partial)

        return data, status_

    def edit_serializer(self, request, user, partial=False):
        serializer = AddSolicitacaoSerializer(
            user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        status_ = status.HTTP_200_OK

        return data, status_

    def check_pk_none(self, pk):
        solicitacao = Solicitacao.objects.filter(pk=pk)

        if len(solicitacao) == 0:

            msg = f'solicitacao com id {pk} não encontrado'
            status_ = status.HTTP_404_NOT_FOUND
            return Response({"error": msg}, status=status_)

        return False

    def get(self, request, pk=None):
        solicitacoes = Solicitacao.objects.all()
        serializer = SolicitacaoSerializer(solicitacoes, many=True)
        return Response({'solicitacoes': serializer.data}, template_name='index.html')

    def post(self, request, format=None):
        serializer = AddSolicitacaoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'form': serializer}, template_name='index.html')
        else:
            return Response({"..":".."} ,status=status.HTTP_201_CREATED)

        # serializer.save()
        return Response({'solicitacoes': serializer.data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        data, status_ = self.edit(request, pk)
        return Response(data, status=status_)

    def patch(self, request, pk, format=None):
        data, status_ = self.edit(request, pk, partial=True)
        return Response(data, status=status_)


