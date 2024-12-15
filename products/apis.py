from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated

from products.models import Products
from .selectors import product_list
from .services import create_product

class ProductCreateView(APIView):
    permission_classes = [IsAuthenticated]
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField()
        price = serializers.DecimalField(max_digits=10, decimal_places=2)
        stock = serializers.IntegerField()
        category = serializers.CharField()
        created_by = serializers.CharField()
    

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = create_product(**serializer.validated_data)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ProductListView(APIView):
    permission_classes = [IsAuthenticated]
    class OutputSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")  # To include category name
        created_by = serializers.CharField(source="created_by.email")  # To include user email

        class Meta:
            model = Products
            fields = ['name', 'description', 'price', 'stock', 'category', 'created_by']

    def get(self, request):
        products = product_list()  # Get QuerySet
        serializer = self.OutputSerializer(products, many=True)  # Pass QuerySet here
        return Response(serializer.data, status=status.HTTP_200_OK)
