from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError

from permissions.mixins import ApiAuthMixin
from .selectors import product_detail, product_list
from .services import create_product, update_product
from .serializers import (
    ProductCreateSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
    ProductUpdateSerializer
)


class ProductCreateApi(ApiAuthMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProductCreateSerializer

    def post(self, request):
        try:
            print("tttt",request.data)
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
                **serializer.validated_data
            )
            response_data = {
                "detail":"product was created successfully",
                "product_id":product.id

            }

            return Response(data=response_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductListApi(ApiAuthMixin, APIView):
    serializer_class = ProductListSerializer

    def get(self, request):
        products = product_list()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailApi(ApiAuthMixin, APIView):
    serializer_class = ProductDetailSerializer()

    def get(self, request, id):
        product = product_detail(id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ProductUpdateApi(ApiAuthMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProductUpdateSerializer

    def put(self, request, id):
        try:
            serializer = ProductUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            images = request.FILES  # Get the list of images
            labels = [request.data.get(f'images[{i}][label]') for i in range(len(images))]  # Get the labels
            # Combine images and labels to send to the update function
            image_data = []
            for idx, image in enumerate(images):
                image_data.append({
                    'image': image,
                    'label': labels[idx] if idx < len(labels) else None
                })  # Get all uploaded images
            update_product(
                images=image_data,  # Pass images list
                product_id = id,
                **serializer.validated_data,
            )
            response_data = {
                "detail":"product was updated successfully",
                "data":serializer.data

            }
            return Response(data=response_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
