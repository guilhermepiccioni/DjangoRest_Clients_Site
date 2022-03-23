from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from core.models import Cliente

from core.serializers import ClienteSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'nome')
    search_fields = ('nome', 'cidade', 'id', 'cep', 'pais', 'endereco')
