from rest_framework import serializers
from .models import FriendRequest
from django.contrib.auth import get_user_model

User = get_user_model()


class RequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ["id", "to_user", "created_at", "status"]

    status = serializers.CharField(source="get_status_display")
    to_user = serializers.StringRelatedField()


class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ["id", "from_user", "to_user"]
        read_only_fields = ("from_user",)

class RequestRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ["id", "from_user", "status", "created_at"]
    from_user = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")

class RequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ["status"]


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ["from_user", "to_user", "status"]

    to_user = serializers.StringRelatedField()
    from_user = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")


class FriendSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
