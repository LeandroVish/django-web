from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
)

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 1


class ListarItensCompraSerializer(ModelSerializer):
    livro = CharField(source="livro.titulo", read_only=True)

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "livro")
        depth = 1


class ListarCompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ListarItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
        usuario = CharField(source="user.email", read_only=True)
        status = CharField(source="get_status_display", read_only=True)
        itens = ItensCompraSerializer(many=True, read_only=True)


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def update(self, compra, validated_data):
        itens_data = validated_data.pop("itens")
        if itens_data:
            compra.itens.all().delete()
            for item_data in itens_data:
                ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return super().update(compra, validated_data)
