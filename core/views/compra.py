from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import (  # novo
    CompraSerializer,
    CriarEditarCompraSerializer,
    ListarCompraSerializer,
)


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ListarCompraSerializer
        if self.action in ("create", "update"):
            return CriarEditarCompraSerializer
        return CompraSerializer
