from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import rules

from permissions.mixins import ApiAuthMixin
from .serializers import UserSerializer, UserUpdateSerializer
from .services import create_user, update_userprofile
from .selectors import user_detail, user_list


class UserCreateApi(ApiAuthMixin, APIView):
    serializer_class = UserSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        if not rules.has_perm("add_user"):
            return Response(
                "You have no Permission to perform this action!",
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = create_user(**serializer.validated_data)
            response_data = {
                "detail": "user was created successfully",
                "user_id": user.id,
            }
            return Response(data=response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserUpdateApi(ApiAuthMixin, APIView):
    serializer_class = UserUpdateSerializer
    parser_classes = (FormParser, MultiPartParser)

    def put(self, request, id):
        if not rules.has_perm("update_user"):
            return Response(
                "You have no Permission to perform this action!",
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            user = update_userprofile(user_id=id, **serializer.validated_data)
            response_data = {
                "detail": "You have successfully updated your profile",
                "user_id": user.id,
                "profile_pic": user.profile_pic.url
                if user.profile_pic
                else None,  # Serialize the profile picture URL
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            return Response(data=response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserListApi(ApiAuthMixin, APIView):
    serializer_class = UserSerializer

    def get(self, request):
        users = user_list()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailApi(ApiAuthMixin, APIView):
    serializer_class = UserSerializer

    def get(self, request, id):
        user = user_detail(id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
