from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import rules
from permissions.mixins import ApiAuthMixin

from .serializers import (
    DiscountCreateSerializer,
    DiscountListSerializer,
    DiscountUpdateSerializer,
    DiscountSerializer,
    DiscountReactivateSerializer,
)
from .services import (
    create_discount,
    deactivate_discount,
    reactivate_discount,
    update_discount,
)
from .selectors import discount_detail_display, discount_list_display


class DiscountCreateApi(ApiAuthMixin, APIView):
    serializer_class = DiscountCreateSerializer

    def post(self, request):
        try:
            if not rules.has_perm("create_discount"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = DiscountCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            create_discount(**serializer.validated_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DiscountListApi(APIView, ApiAuthMixin):
    def get(self, request):
        try:
            if not rules.has_perm("view_discount"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            discounts = discount_list_display()
            serializer = DiscountListSerializer(discounts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DiscountDetailApi(APIView):
    def get(self, request, discount_id):
        try:
            if not rules.has_perm("view_discount"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            discount = discount_detail_display(discount_id)
            serializer = DiscountSerializer(discount)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DiscountUpdateApi(ApiAuthMixin, APIView):
    serializer_class = DiscountUpdateSerializer

    def put(self, request, discount_id):
        try:
            if not rules.has_perm("update_discount"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = DiscountUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            update_discount(discount_id, **serializer.validated_data)

            return Response("Discount updated", status=status.HTTP_202_ACCEPTED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DiscountDeactivateApi(ApiAuthMixin, APIView):
    def put(self, request, id):
        try:
            if not rules.has_perm("deactivate_discount"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            deactivate_discount(discount_id=id)

            return Response(
                {"Detail": "Discount deactivated"}, status=status.HTTP_202_ACCEPTED
            )

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DiscountReactivateApi(ApiAuthMixin, APIView):
    serializer_class = DiscountReactivateSerializer

    def put(self, request, id):
        try:
            if not rules.has_perm("reactivate_discount"):
                return Response(
                    "You have no Permission to perform this action!",
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = DiscountReactivateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            reactivate_discount(discount_id=id, **serializer.validated_data)

            return Response(
                {"Detail": "Discount reactivated"}, status=status.HTTP_202_ACCEPTED
            )

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
