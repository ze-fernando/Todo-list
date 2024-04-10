from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as gl


class CustomUserManager(BaseUserManager):
    def create_user(self, username, age, tel, password=None):

        if not username:
            raise ValueError(gl("The username must be set"))

        username = self.normalize_username(username)
        user = self.model(username=username, age=age, tel=tel)
        user.set_password(password)
        user.save(using=self._db)
        return user
