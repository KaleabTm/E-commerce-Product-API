from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated

from permissions.mixins import ApiAuthMixin
from .models import Products
from .selectors import product_list
from .services import create_product
from .serializers import ProductDetailSerializer, ProductListSerializer

class ProductCreateView(ApiAuthMixin, APIView):
    def post(self, request):
        serializer = ProductDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            create_product(**serializer.validated_data)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ProductListView(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name") 
        created_by = serializers.CharField(source="created_by.email")

        class Meta:
            model = Products
            fields = ['name', 'description', 'price', 'stock', 'category', 'created_by']

    def get(self, request):
        products = product_list()
        serializer = self.OutputSerializer(products, many=True)  # Pass QuerySet here
        return Response(serializer.data, status=status.HTTP_200_OK)
