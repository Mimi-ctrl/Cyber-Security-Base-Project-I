from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=200)
