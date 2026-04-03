from django.db import models

# Role model
class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField('Permission', related_name='roles')

# User model
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    roles = models.ManyToManyField(Role, related_name='users')

# Permission model
class Permission(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()