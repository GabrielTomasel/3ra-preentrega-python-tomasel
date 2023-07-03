from django.db import models

class Comunication(models.Model):
    message_name = models.CharField(max_length=25)
    message = models.CharField(max_length=200)