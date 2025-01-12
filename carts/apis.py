from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rules
from permissions.mixins import ApiAuthMixin
from rest_framework.exceptions import ValidationError

from .serializers import CartItemListSerializer, cartItemSerializer
from .services import add_to_cart, remove_cart_item, update_cart_item_quantity
from .selectors import cart_item_list, cart_item_detail, get_cart


class CartItemCreateApi(ApiAuthMixin, APIView):
    serializer_class = cartItemSerializer

    def post(self, request):
        try:
            if not rules.has_perm("add_cart_item"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = cartItemSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            add_to_cart(user=request.user, **serializer.validated_data)

            return Response(
                "Item added to cart successfuly", status=status.HTTP_201_CREATED
            )

        except ValidationError as e:
            raise ValidationError(e)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CartItemUpdateApi(ApiAuthMixin, APIView):
    serializer_class = cartItemSerializer

    def put(self, request, id):
        try:
            if not rules.has_perm("update_cart_item"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = cartItemSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            update_cart_item_quantity(cart_item_id=id, **serializer.validated_data)

            return Response("Item quantity updated", status=status.HTTP_202_ACCEPTED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CartItemDeleteApi(ApiAuthMixin, APIView):
    def delete(self, request, id):
        try:
            if not rules.has_perm("delete_cart_item"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            remove_cart_item(cart_item_id=id)

            return Response(
                "Item Removed successfuly", status=status.HTTP_204_NO_CONTENT
            )

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CartItemListViewApi(ApiAuthMixin, APIView):
    serializer_class = CartItemListSerializer

    def get(self, request):
        try:
            if not rules.has_perm("view_cart_item"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            cart = get_cart(user=request.user)
            print("dd", cart)
            cart_items = cart_item_list(cart=cart)

            serializer = CartItemListSerializer(cart_items, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CartItemDetailViewApi(ApiAuthMixin, APIView):
    serializer_class = CartItemListSerializer

    def get(self, request, id):
        try:
            if not rules.has_perm("view_cart_item"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            cart_item = cart_item_detail(id=id)

            output_data = CartItemListSerializer(cart_item).data

            return Response(output_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
