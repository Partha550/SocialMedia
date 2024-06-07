from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.throttling import UserRateThrottle

from .models import FriendRequest
from .serializers import (
    FriendListSerializer,
    FriendSearchSerializer,
    RequestCreateSerializer,
    RequestListSerializer,
    RequestRetrieveSerializer,
    RequestUpdateSerializer,
)

# Create your views here.
User = get_user_model()


class SendFriendRequestThrottle(UserRateThrottle):
    scope = "post"
    rate = "3/min"

    def allow_request(self, request, view):
        if request.method == "GET":
            return True
        return super().allow_request(request, view)


class RequestListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ("status",)
    throttle_classes = [SendFriendRequestThrottle]

    def get_serializer_class(self):
        if self.request.method == "GET":
            self.serializer_class = RequestListSerializer
        elif self.request.method == "POST":
            self.serializer_class = RequestCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        from_user = self.request.user
        serializer.validated_data["from_user"] = from_user
        return super().perform_create(serializer)

    def get_queryset(self):
        user = self.request.user
        queryset = FriendRequest.objects.filter(from_user=user)
        return queryset


class RequestIncomingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RequestRetrieveSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = FriendRequest.objects.filter(to_user=user)
        return queryset


class RequestAcceptRejectView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = FriendRequest.objects.filter(to_user=user)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            self.serializer_class = RequestRetrieveSerializer
        elif self.request.method == "PUT":
            self.serializer_class = RequestUpdateSerializer
        return super().get_serializer_class()


class ListFriends(generics.ListAPIView):
    serializer_class = FriendListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        q = (Q(from_user=user) | Q(to_user=user)) & Q(status="A")
        return FriendRequest.objects.filter(q)


class SearchFriends(generics.ListAPIView):
    serializer_class = FriendSearchSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        word = self.request.query_params.get("q", "")
        q = (
            Q(email__exact=word)
            | Q(first_name__icontains=word)
            | Q(last_name__icontains=word)
        )
        self.queryset = User.objects.filter(q)
        return super().get_queryset()
