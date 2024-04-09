from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as gl


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):

        if not username:
            raise ValueError(gl("The username must be set"))

        username = self.normalize_username(username)
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user
