from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .services import create_category
from rest_framework.permissions import IsAuthenticated


class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField()

    serializer_class = InputSerializer

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

        create_category(**serializer._validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
