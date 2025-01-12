from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
import rules
from permissions.mixins import ApiAuthMixin


from .serializers import (
    OrderCreateSerializer,
    OrderDetailSerializer,
    OrderItemSerializer,
)
from .services import (
    place_order_cart,
    approve_order,
    create_order_item,
    cancel_order,
    update_order,
    place_order_cart_all,
)
from .selectors import order_item_detail, get_order


class PlaceOrderApi(ApiAuthMixin, APIView):
    serializer_class = OrderCreateSerializer

    def post(self, request):
        try:
            if not rules.has_perm("create_order"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            serializer = OrderCreateSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            print("ser", serializer.validated_data)

            order = create_order_item(user=request.user.id, **serializer.validated_data)

            return Response(
                {"detail": "Order placed successfully.", "order_id": order.id},
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PlaceOrderCartApi(ApiAuthMixin, APIView):
    serilaizer_class = OrderItemSerializer

    def post(self, request):
        serializer = self.serilaizer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            if not rules.has_perm("create_order"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            place_order_cart(**serializer.validated_data)

            return Response(
                "Your order has been created successfully",
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class OrderCancelApi(APIView):
    def post(self, request, order_id):
        try:
            cancel_order(order_id)
            return Response(
                {"detail": f"Order {order_id} has been successfully cancelled."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateApi(APIView):
    def put(self, request, id):
        data = request.data
        try:
            if not rules.has_perm("update_order"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            update_order(order_id=id, **data)
            return Response(
                {"detail": f"Order {id} has been successfully updated."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderApproveApi(APIView):
    def post(self, request, id):
        try:
            if not rules.has_perm("approve_order"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            approve_order(order_id=id)
            return Response(
                {"detail": f"Order {id} has been successfully approved."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PlaceOrderCartAllApi(APIView):
    def post(self, request):
        try:
            if not rules.has_perm("create_order"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            order = place_order_cart_all(user=request.user)
            return Response(
                {"detail": "Order placed successfully.", "order_id": order.id},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderItemListViewApi(ApiAuthMixin, APIView):
    serializer_class = OrderDetailSerializer

    def get(self, request):
        try:
            if not rules.has_perm("view_order"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            order = get_order(user=request.user)

            serializer = OrderDetailSerializer(order, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class OrderItemDetailViewApi(ApiAuthMixin, APIView):
    serializer_class = OrderDetailSerializer

    def get(self, request, id):
        try:
            if not rules.has_perm("view_order"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )
            order_item = order_item_detail(id=id)

            output_data = OrderDetailSerializer(order_item).data

            return Response(output_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
