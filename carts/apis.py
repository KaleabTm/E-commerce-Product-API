from rest_framework.views import APIView
from permissions.mixins import ApiAuthMixin
from .serializers import cartItemCreateSerializer


class CartItemCreate(ApiAuthMixin, APIView):
    serializer_class = cartItemCreateSerializer
