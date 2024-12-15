from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .services import create_category


class CategoryCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField()
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        cat = create_category(**serializer._validated_data)
        

        return Response(serializer.data,status=status.HTTP_201_CREATED)
        

        

