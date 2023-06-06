from django.db import models

class UserInfoModel(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    location = models.JSONField()

    def __str__(self):
        return self.email
