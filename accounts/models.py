from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, UserManager


class User(models.Model):
	email = models.EmailField(primary_key=True)
	REQUIRED_FIELDS = ()
	USERNAME_FIELD = 'email'

	objects = UserManager()

	def is_authenticated(self):
		return True

	def set_password(**kwargs):
		return super().set_password(**kwargs)
