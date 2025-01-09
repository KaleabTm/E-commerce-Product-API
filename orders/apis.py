from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from permissions.mixins import ApiAuthMixin
from rest_framework.exceptions import ValidationError


from .serializers import OrderCreateSerializer, OrderDetailSerializer, OrderItemSerializer
from .services import place_order_cart, approve_order, create_order_item


class PlaceOrderApi(ApiAuthMixin, APIView):
    serializer_class = OrderCreateSerializer

    def post(self,request):
        try:
            serializer = OrderCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            create_order_item(**serializer.validated_data)

            return Response("Your order has been created successfully", status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PlaceOrderCartApi(ApiAuthMixin, APIView):
    serilaizer_class = OrderItemSerializer