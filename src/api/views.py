from .serializers import *
from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(token),
            'access': str(token.access_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ForumViewSet(ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class LikeForumViewSet(ModelViewSet):
    queryset = LikeForum.objects.all()
    serializer_class = LikeForumSerializer


class LikeMessageViewSet(ModelViewSet):
    queryset = LikeMessage.objects.all()
    serializer_class = LikeMessageSerializer


class SubscribeViewSet(ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer


