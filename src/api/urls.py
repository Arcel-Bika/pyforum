from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (RegisterViewSet, RoleViewSet, CategoryViewSet,
                    ForumViewSet, MessageViewSet, LikeForumViewSet, SubscribeViewSet, LikeMessageViewSet)


router = DefaultRouter()

router.register("user", RegisterViewSet)
router.register("role", RoleViewSet)
router.register("category", CategoryViewSet)
router.register("forum", ForumViewSet)
router.register("message", MessageViewSet)
router.register("like-forum", LikeForumViewSet)
router.register("like-message", LikeMessageViewSet)
router.register("subscribe", SubscribeViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

