from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None, phone_user=None, city=None):
        if not email:
            raise ValueError("Votre adresse mail est invalide.")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_user=phone_user,
            city=city,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, city, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            city=city,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


if __name__ == "__main__":
    MyUserManager()

