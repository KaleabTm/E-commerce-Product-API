from django.forms import ValidationError
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from .services import create_user

# Create your views here.


class Login(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(write_only=True)

    serializer_class = InputSerializer

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, user)

        session_id = request.session.session_key

        return Response(
            {"detail": "User logged in successfully", "session_id": session_id},
            status=status.HTTP_200_OK,
        )


class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {"detail": "You have logged out successfully"}, status=status.HTTP_200_OK
        )


class RegisterApi(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(
            write_only=True, required=True
        )  # Make password required

    serializer_class = InputSerializer

    def post(self, request):
        try:
            print("Request data:", request.data)
            input_serializer = self.serializer_class(data=request.data)
            input_serializer.is_valid(raise_exception=True)

            # Creating the user via the service function
            user_instance = create_user(**input_serializer.validated_data)

            response_data = {
                "message": "Your account has been successfully created.",
                "email": user_instance.email,
            }

            return Response(data=response_data, status=status.HTTP_200_OK)

        except ValidationError as e:
            # DRF will handle this exception by default, so you can skip re-raising it
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle any other unexpected errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    