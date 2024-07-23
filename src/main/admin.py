from django.contrib import admin
from .models import CustomUser, Role, Category, Forum, Message, LikeForum, LikeMessage, Subscribe

admin.site.register(CustomUser)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Forum)
admin.site.register(Message)
admin.site.register(LikeForum)
admin.site.register(LikeMessage)
admin.site.register(Subscribe)
