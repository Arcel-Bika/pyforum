from rest_framework.serializers import ModelSerializer
from main.models import *


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ForumSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class LikeForumSerializer(ModelSerializer):
    class Meta:
        model = LikeForum
        fields = "__all__"


class LikeMessageSerializer(ModelSerializer):
    class Meta:
        model = LikeMessage
        fields = "__all__"


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"

