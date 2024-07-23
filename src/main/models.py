from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from create_user import MyUserManager


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=200, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'city', 'password']

    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Role(models.Model):
    type_role = models.CharField(max_length=50)

    def __str__(self):
        return f'Role: {self.type_role}'


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    description_category = models.TextField(max_length=1000)
    slug_category = models.SlugField()

    def __str__(self):
        return f'Categorie : {self.name_category}'


class Forum(models.Model):
    subject = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    autor_forum = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug_forum = models.SlugField()

    def __str__(self):
        return f'Sujet : {self.subject}'


class Message(models.Model):
    description_message = models.TextField(max_length=500)
    date_message = models.DateTimeField(auto_now_add=True)
    autor_message = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    forum_message = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return f'Auteur: {self.autor_message}'


class LikeForum(models.Model):
    nomber_likes = models.IntegerField()
    forum_like = models.ForeignKey(Forum, on_delete=models.CASCADE)
    autor_like_for = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Le forum {self.forum_like} a {self.nomber_likes} likes'


class LikeMessage(models.Model):
    nomber_likes = models.IntegerField()
    message_like = models.ForeignKey(Message, on_delete=models.CASCADE)
    autor_like_msg = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Le message {self.message_like} a {self.nomber_likes} likes'


class Subscribe(models.Model):
    autor_sub = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    forum_sub = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.autor_sub} s\'est abonné(e) à {self.forum_sub}'

