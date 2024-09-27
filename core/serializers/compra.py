from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField


from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 1
class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        usuario = CharField(source="user.email", read_only=True)  # inclua essa linha
        status = CharField(source="get_status_display", read_only=True)  # inclua essa linha
        itens = ItensCompraSerializer(many=True, read_only=True)
