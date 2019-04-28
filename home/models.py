from django.db import models

class Contact(models.Model):

    name = models.CharField(default="John Doe", max_length=100)
    relationship = models.CharField(default=1, max_length=100)
    carrier = models.CharField(default="att", choices=[(m,m) for m in ['att', 'tmobile', 'verizon', 'sprint']], max_length=100)
    number = models.CharField(default="1231230000", max_length=100)

class Options(models.Model):

    number = models.CharField(default="1231230000", max_length=100)
    carrier = models.CharField(default="att", choices=[(m,m) for m in ['att', 'tmobile', 'verizon', 'sprint']], max_length=100)
    cheap = models.IntegerField(default=2)
    expensive = models.IntegerField(default=3)
    popular = models.FloatField(default=3)
