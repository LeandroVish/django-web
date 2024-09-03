from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        usuario = CharField(source="user.email", read_only=True)  # inclua essa linha
