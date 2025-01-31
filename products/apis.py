from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from permissions.mixins import ApiAuthMixin
from .filters import filter_products
from .selectors import product_detail, product_list
from .services import create_product, update_product
from .serializers import (
    ProductCreateSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
    ProductUpdateSerializer,
)

import rules


class ProductCreateApi(ApiAuthMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProductCreateSerializer

    def post(self, request):
        try:
            if not rules.has_perm("add_product"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            serializer = ProductCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            images = []
            for key, file in request.FILES.items():
                if key.startswith("images[") and key.endswith("[image]"):
                    index = key.split("[")[1].split("]")[0]  # Extract the index
                    label_key = f"images[{index}][label]"
                    label = request.data.get(label_key, None)
                    images.append({"image": file, "label": label})

            product = create_product(
                created_by=request.user,
                images=images,  # Pass images list
                **serializer.validated_data,
            )
            response_data = {
                "detail": "product was created successfully",
                "product_id": product.id,
            }

            return Response(data=response_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ProductListApi(ApiAuthMixin, APIView):
    serializer_class = ProductListSerializer

    def get(self, request):
        products = product_list()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailApi(ApiAuthMixin, APIView):
    serializer_class = ProductDetailSerializer()

    def get(self, request, id):
        if not rules.has_perm("view_product"):
            return Response(
                "You have no Permission to perform this action!",
                status=status.HTTP_403_FORBIDDEN,
            )
        product = product_detail(id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductUpdateApi(ApiAuthMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProductUpdateSerializer

    def put(self, request, id):
        try:
            if not rules.has_perm("update_product"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            serializer = ProductUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            images = request.FILES  # Get the list of images
            labels = [
                request.data.get(f"images[{i}][label]") for i in range(len(images))
            ]  # Get the labels
            # Combine images and labels to send to the update function
            image_data = []
            for idx, image in enumerate(images):
                image_data.append(
                    {
                        "image": image,
                        "label": labels[idx] if idx < len(labels) else None,
                    }
                )  # Get all uploaded images
            update_product(
                images=image_data,  # Pass images list
                product_id=id,
                **serializer.validated_data,
            )
            response_data = {
                "detail": "product was updated successfully",
                "data": serializer.data,
            }
            return Response(data=response_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ProductSearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductSearchApi(APIView):
    pagination_class = ProductSearchPagination

    def get(self, request):
        if not rules.has_perm("view_product"):
            return Response(
                "You have no Permission to perform this action!",
                status=status.HTTP_403_FORBIDDEN,
            )
        query = request.query_params.get("query", "").strip()
        category = request.query_params.get("category", "").strip()

        # Call the filter function
        filtered_products = filter_products(query=query, category=category)

        # Paginate results
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(filtered_products, request)
        serializer = ProductListSerializer(paginated_queryset, many=True)

        return paginator.get_paginated_response(serializer.data)
