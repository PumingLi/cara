from django.db import models

class Contact(models.Model):

    name = models.CharField(default="John Doe", max_length=100)
    relationship = models.CharField(default=1, max_length=100)
    number = models.CharField(default="(123)-123-0000", max_length=100)
