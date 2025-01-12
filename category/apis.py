from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from permissions.mixins import ApiAuthMixin


from .serializers import CategorySerializer, CategoryCreateSerializer
from .services import create_category, delete_category, update_category
from .selectors import category_list, category_detail


class CategoryCreateView(ApiAuthMixin, APIView):
    serializer_class = CategoryCreateSerializer

    def post(self, request):
        try:
            serializer = CategoryCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            create_category(**serializer._validated_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CategoryListView(APIView):
    def get(self, request):
        try:
            categories = category_list()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CategoryDetailView(APIView):
    def get(self, request, category_id):
        try:
            category = category_detail(category_id=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CategoryUpdateView(ApiAuthMixin, APIView):
    serializer_class = CategoryCreateSerializer

    def put(self, request, category_id):
        try:
            serializer = CategoryCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            update_category(category_id=category_id, **serializer.validated_data)

            return Response("Category updated", status=status.HTTP_202_ACCEPTED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CategoryDeleteView(ApiAuthMixin, APIView):
    def delete(self, request, category_id):
        try:
            delete_category(category_id=category_id)

            return Response(
                "Category Removed successfuly", status=status.HTTP_204_NO_CONTENT
            )

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
