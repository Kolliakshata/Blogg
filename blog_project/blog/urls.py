from django.urls import path
from .views import PostListCreateView, PostDetailView, BlockedUserListView, BlockedUserDetailView

urlpatterns = [
    path('api/posts/', PostListCreateView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/get-blocked-users/', BlockedUserListView.as_view(), name='blocked-user-list'),
    path('api/block-user/', BlockedUserListView.as_view(), name='block-user'),
    path('api/unblock-user/', BlockedUserDetailView.as_view(), name='unblock-user'),
]

