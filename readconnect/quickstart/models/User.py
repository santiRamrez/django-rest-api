from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # WannaRead is going to save a string separated by comma with the PK of several books.
    wannaRead = models.CharField(max_length=100, default=0)
    # HaveReaded is going to save a string separated by comma with the PK of several books.
    haveReaded = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=20, default=0)
    created_at = models.DateTimeField(auto_now_add=True)