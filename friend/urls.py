from django.urls import path
from .views import (
    ListFriends,
    RequestAcceptRejectView,
    RequestIncomingListView,
    RequestListCreateView,
    SearchFriends,
)

urlpatterns = [
    path("egressrequests", RequestListCreateView.as_view()),
    path("ingresrequests", RequestIncomingListView.as_view()),
    path("ingresrequests/<int:pk>/", RequestAcceptRejectView.as_view()),
    path("myfriends", ListFriends.as_view()),
    path("search", SearchFriends.as_view()),
]
