# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **other_fields):
               
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **other_fields):
        
        # veryacademy
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        ##
        
        if password is None:
            raise TypeError('Password should not be none')
        
        # veryacademy
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        ##

        user = self.create_user(username, email, password, **other_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


#AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
#                  'twitter': 'twitter', 'email': 'email'}

AUTH_PROVIDERS = {'email': 'email'}

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    # first_name = models.CharField(
    #     max_length=255, unique=True, db_index=True, default=None)
    # last_name = models.CharField(max_length=255, unique=True, db_index=True, default=None)
    # role = models.TextField(_(
    #     'role'), max_length=500, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # start_date = models.DateField(
    #     "Entry date dd/mm/yyyy", auto_now_add=False, auto_now=False, blank=True, null=False, default=None)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Profile(models.Model):
 	username = models.OneToOneField(
 	    User, on_delete=models.CASCADE, related_name='profile',default=None)
 	first_name = models.CharField(max_length=200, null=True, blank=True)
 	last_name = models.CharField(max_length=200, null=True, blank=True)
 	phone = models.CharField(max_length=200, null=True, blank=True)

 	def __str__(self):
 		return str(self.username)


class Order(models.Model):
    user_status = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_status')
    user_created = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_was_created')
    user_modified = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_was_modified')
