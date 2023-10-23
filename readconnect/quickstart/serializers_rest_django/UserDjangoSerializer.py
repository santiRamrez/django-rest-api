from django.contrib.auth.models import User
from rest_framework import serializers

class UserDjangoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']