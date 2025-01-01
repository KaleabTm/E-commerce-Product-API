from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from permissions.mixins import ApiAuthMixin
from .selectors import product_detail, product_list
from .services import create_product
from .serializers import (
    ProductCreateSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
)


class ProductCreateView(ApiAuthMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProductCreateSerializer

    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            create_product(**serializer.validated_data)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductListView(ApiAuthMixin, APIView):
    serializer_class = ProductListSerializer

    def get(self, request):
        products = product_list()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(ApiAuthMixin, APIView):
    serializer_class = ProductDetailSerializer()

    def get(self, request, product_id):
        product = product_detail(product_id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
