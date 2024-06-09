from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserCreateSerializer, UserSerializer

User = get_user_model()


# Create your views here.
class UserSignup(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        User.objects.create_user(**data)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None):
        if request.user:
            data = UserSerializer(request.user).data
            return Response(data)


