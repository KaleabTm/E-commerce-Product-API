from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    profile_pic = serializers.ImageField()
    phone_number = serializers.IntegerField(required=False, allow_null=True)
    email = serializers.EmailField()
    password = serializers.CharField()
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    address = serializers.CharField(required=False, allow_null=True)
    role = serializers.CharField(required=False, allow_null=True)


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    profile_pic = serializers.ImageField(required=False, allow_null=True)
    phone_number = serializers.IntegerField(required=False, allow_null=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    address = serializers.CharField(required=False, allow_null=True)
