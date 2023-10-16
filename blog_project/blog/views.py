# posts/views.py
from rest_framework import generics
from .models import Post, BlockedUser
from .serializers import PostSerializer, BlockedUserSerializer
from .permissions import IsOwnerOrSuperuser

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrSuperuser]

class BlockedUserListView(generics.ListCreateAPIView):
    queryset = BlockedUser.objects.all()
    serializer_class = BlockedUserSerializer

class BlockedUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlockedUser.objects.all()
    serializer_class = BlockedUserSerializer
    permission_classes = [IsOwnerOrSuperuser]


